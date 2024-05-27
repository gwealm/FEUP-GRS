from typing import List, Optional
from datetime import datetime
import os

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from pydantic import BaseModel

from dotenv import load_dotenv
from engine.docker.compose import DockerCompose
from engine.docker.compose.manifest import Manifest
from engine.docker.compose.models.network import IPAM as DockerIPAM
from engine.docker.compose.models.network import IPAMConfig as DockerIPAMConfig
from engine.docker.compose.models.network import Network as DockerNetwork
from engine.docker.compose.models.service import NetworkSpec as DockerNetworkSpec
from engine.docker.compose.models.service import Service as DockerService

# Importing Network, CIDR, IPAddress
from engine.models.network import CIDR, IPAddress, Network

load_dotenv()  # Load environment variables from .env file


# TODO: need to have: image, custom scripts (?), IP
class Service(BaseModel):
    """Model representing a service."""

    id: str
    name: str
    description: Optional[str] = None
    image: Optional[str] = None
    tag: Optional[str] = None


# TODO: need to have: CIDR, services with IPs (single-router setup needs to have the last IP)
class Team(BaseModel):
    """Model representing a team."""

    id: int
    name: str
    description: Optional[str] = None
    cidr: str
    services: List[Service]
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class Organization(BaseModel):
    """Model representing an organization."""

    id: int
    name: str
    teams: List[Team]


class Database:
    """Class for managing database interactions with MongoDB."""

    def __init__(self):
        uri = os.getenv("MONGODB_URI")
        db_name = os.getenv("MONGODB_DB_NAME")

        if not uri or not db_name:
            raise EnvironmentError("MONGODB_URI and MONGODB_DB_NAME must be set")

        self.client = MongoClient(uri)
        self.db = self.client[db_name]

        self.org_collection = self.db["organizations"]

        self.team_collection = self.db["teams"]

        self.service_collection = self.db["services"]

        self.compose = DockerCompose()

    def get_services(self) -> list[Service]:
        """Get all services."""

        services = []

        for service in self.service_collection.find():
            service['id'] = str(service["_id"])
            del service["_id"]

            services.append(Service(**service))

        return services

    def get_next_org_id(self) -> int:
        """Get the next organization ID."""
        last_org = self.org_collection.find_one(sort=[("id", -1)])
        return last_org["id"] + 1 if last_org else 1

    def create_org(self, org: Organization):
        """Create a new organization."""
        try:
            self.org_collection.insert_one(org.model_dump())
        except DuplicateKeyError as exc:
            raise ValueError("Organization with this ID already exists.") from exc

    def get_org(self, org_id: int) -> Optional[Organization]:
        """Retrieve an organization by ID."""
        org_data = self.org_collection.find_one({"id": org_id})
        if org_data:
            return Organization(**org_data)
        return None

    def update_org(self, org_id: int, org: Organization):
        """Update an existing organization."""
        self.org_collection.update_one({"id": org_id}, {"$set": org.model_dump()})

    def delete_org(self, org_id: int):
        """Delete an organization by ID."""
        self.org_collection.delete_one({"id": org_id})

    def create_team(self, org_id: int, team: Team):
        """Add a team to an existing organization."""

        org = self.get_org(org_id)

        if org:
            org.teams.append(team)
            self.update_org(org.id, org)

            team_subnet_cidr = CIDR.from_string(team.cidr)

            team_network = Network(f"{team.name}-network", cidr=team_subnet_cidr)

            # TODO: this would use engine-agnostic models
            team_docker_network = DockerNetwork(
                name=team_network.name,
                ipam=DockerIPAM(
                    config=[
                        DockerIPAMConfig(
                            subnet=str(team_network.cidr),
                        )
                    ]
                ),
            )

            services: dict[str, DockerService] = {}

            # Deploy services when a team is created
            for teamService in team.services:
                serviceAddress = team_network.next_host_address()

                # TODO: these should be handled by model converters
                dockerService = DockerService(
                    image="",  # TODO: get image from service
                    networks={
                        team_docker_network.name: DockerNetworkSpec(
                            ipv4_address=str(serviceAddress),
                        )
                    },
                    command=None,  # TODO: might need a custom command for additional setup, like setting up scripts or variables inside the container
                )

                services[teamService.name] = dockerService

            manifest = Manifest(
                services=services,
                networks={team_docker_network.name: team_docker_network},
            )

            # TODO: configure router, routes, DNS, etc etc

    def delete_team(self, org_id: int, team_id: int):
        """Remove a team from an existing organization."""
        org = self.get_org(org_id)
        if org:
            team = next((t for t in org.teams if t.id == team_id), None)
            if team:
                # Tear down services before deleting the team
                for service in team.services:
                    manifest = self._create_manifest(service)
                    self.compose.tear_down(manifest)
                org.teams = [t for t in org.teams if t.id != team_id]
                self.update_org(org_id, org)

    def deploy_service(self, org_id: int, team_id: int, service: Service):
        """Deploy a new service for a team."""
        org = self.get_org(org_id)
        if org:
            for team in org.teams:
                if team.id == team_id:
                    service.ipAddress = self._assign_ip_address(team.cidr)
                    team.services.append(service)
                    self.update_org(org_id, org)
                    manifest = self._create_manifest(service)
                    self.compose.provision(manifest)

    def stop_service(self, org_id: int, team_id: int, service_name: str):
        """Stop a service of a team."""
        org = self.get_org(org_id)
        if org:
            for team in org.teams:
                if team.id == team_id:
                    service = next(
                        (s for s in team.services if s.name == service_name), None
                    )
                    if service:
                        manifest = self._create_manifest(service)
                        self.compose.tear_down(manifest)

    def start_service(self, org_id: int, team_id: int, service_name: str):
        """Start a service for a team."""
        org = self.get_org(org_id)
        if org:
            for team in org.teams:
                if team.id == team_id:
                    service = next(
                        (s for s in team.services if s.name == service_name), None
                    )
                    if service:
                        manifest = self._create_manifest(service)
                        self.compose.provision(manifest)

    def _create_manifest(self, service: Service) -> Manifest:
        """Create a Manifest object from a Service."""
        services = {
            service.name: DockerService(
                image="example_image", ports=["80"], environment=[]
            )
        }
        return Manifest(services=services)

    def _assign_ip_address(self, cidr_str: str) -> str:
        """Assigns an IP address from the given CIDR block."""
        cidr = CIDR.from_string(cidr_str)
        network = Network("team_network", cidr)
        ip_address = network.next_host_address()
        return str(ip_address)
