"""
"""
from typing import List, Optional
from datetime import datetime
import os

from pymongo import MongoClient
from bson import ObjectId
from bson import DBRef
from pydantic import BaseModel

from dotenv import load_dotenv
from engine.docker.compose import DockerCompose
from engine.docker.compose.handler import DockerComposeManifestHandler
from engine.docker.compose.manifest import Manifest
from engine.docker.compose.models.service import NetworkSpec as DockerNetworkSpec
from engine.docker.compose.models.service import Service as DockerService

# Importing Network, CIDR, IPAddress
from engine.models.network import CIDR, Network

load_dotenv()  # Load environment variables from .env file

# FIXME: THIS FILE DOES TO MUCH BUT I CAN'T BE ARSED RIGHT NOW


# TODO: need to have: image, custom scripts (?), IP
class Service(BaseModel):
    """Model representing a service."""

    id: str
    name: str
    slug: str
    description: Optional[str] = None
    image: Optional[str] = None
    tag: Optional[str] = None
    deployedAt: Optional[str] = None
    ipAddress: Optional[str] = None


# TODO: need to have: CIDR, services with IPs (single-router setup needs to have the last IP)
class TeamCreationRequestPayload(BaseModel):
    """Model representing a team."""

    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    cidr: str
    services: List[str]

class Team(BaseModel):
    """Model representing a team."""

    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    cidr: str
    services: List[Service]
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class Database:
    """Class for managing database interactions with MongoDB."""

    def __init__(self):
        uri = os.getenv("MONGODB_URI")
        db_name = os.getenv("MONGODB_DB_NAME")

        if not uri or not db_name:
            raise EnvironmentError("MONGODB_URI and MONGODB_DB_NAME must be set")

        self.client = MongoClient(uri)
        self.db = self.client[db_name]

        self.team_collection = self.db["teams"]
        self.team_collection.create_index({"_id": 1})

        self.service_collection = self.db["services"]
        self.service_collection.create_index({"_id": 1})

        self.compose = DockerCompose()
        self.handler = DockerComposeManifestHandler()

        self.manifest_template = self.handler.load(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "templates", "team-template.yml")) # FIXME: black magic

    def get_services(self) -> list[Service]:
        """Get all services."""

        services = []

        for service in self.service_collection.find():
            service["id"] = str(service["_id"])
            del service["_id"]

            services.append(Service(**service))

        return services

    def get_service(self, service_id: int) -> Optional[Service]:
        """Get a service by id."""

        service = self.service_collection.find_one(ObjectId(service_id))

        if not service:
            return None

        service["id"] = str(service["_id"])
        del service["_id"]

        return Service(**service)

    def get_teams(self) -> list[Service]:
        """Get all teams."""

        teams = []

        for team in self.team_collection.find():
            team["id"] = str(team["_id"])
            del team["_id"]

            services = []
            for service in team["services"]:

                service_ref = service["ref"]
                deployed_at = service["deployed_at"]
                ip_address = service["ip_address"]

                service = self.get_service(service_ref.id)
                service.deployedAt = deployed_at
                service.ipAddress = ip_address

                services.append(service)

            team["services"] = services
            teams.append(Team(**team))

        return teams

    def get_team(self, team_id: int) -> Optional[Team]:
        """Get a team by id."""

        team = self.team_collection.find_one(ObjectId(team_id))

        if not team:
            return None

        team["id"] = str(team["_id"])
        del team["_id"]

        services = []
        for service in team["services"]:

            service_ref = service["ref"]
            deployed_at = service["deployed_at"]
            ip_address = service["ip_address"]

            service = self.get_service(str(service_ref.id))
            service.deployedAt = deployed_at
            service.ipAddress = ip_address

            services.append(service)

        team["services"] = services

        return Team(**team)

    def create_team(self, team_spec: TeamCreationRequestPayload) -> Team:
        """Add a team to an existing organization."""

        team_subnet_cidr = CIDR.from_string(team_spec.cidr)

        team_name_escaped = team_spec.name.replace(' ', '-')

        team_network = Network(f"{team_name_escaped}-network", cidr=team_subnet_cidr)
        _gateway_ip = team_network.next_host_address()

        manifest_vars = {
            "teamname": team_name_escaped,
            "subnet": str(team_subnet_cidr),
            "web_ip": str(team_network.next_host_address()),
            "proxy_ip": str(team_network.next_host_address()),
            "dns_ip": str(team_network.next_host_address()),
        }

        manifest = self.manifest_template.compile(manifest_vars)

        team_spec_data = team_spec.model_dump()

        team_services_ids = team_spec_data['services']
        del team_spec_data['services']

        services: dict[str, DockerService] = {}
        team_services = []

        # Deploy services when a team is created
        for team_service_id in team_services_ids:

            service = self.get_service(team_service_id)

            service_address = team_network.next_host_address()

            service_name = f"{team_name_escaped}_{service.slug}"

            # TODO: these should be handled by model converters
            docker_service = DockerService(
                image=service.image,  # TODO: get image from service
                networks={
                    f"{team_name_escaped}_net": DockerNetworkSpec(
                        ipv4_address=str(service_address),
                    )
                },
                command=None,  # TODO: might need a custom command for additional setup, like setting up scripts or variables inside the container
                container_name=service_name
            )

            services[service_name] = docker_service
            team_services.append({"ref": DBRef(collection='services', id=team_service_id), "deployed_at": datetime.now(), "ip_address": str(service_address)})

        result = self.team_collection.insert_one(
            {
                **team_spec_data,
                "services": team_services,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now(),
            }
        )

        manifest.services.update(services)

        print(self.compose.handler.dump(manifest))

        self.compose.provision(manifest)

        team = self.get_team(result.inserted_id)

        return team

        # TODO: configure router, routes, DNS, etc etc

    def delete_team(self, team_id: int):
        """Remove a team from an existing organization."""

        team = self.get_team(team_id)

        team_subnet_cidr = CIDR.from_string(team.cidr)
        team_network = Network(f"{team.name}-network", cidr=team_subnet_cidr)
        team_network.next_host_address() # skip gateway

        team_name_escaped = team.name.replace(' ', '-')

        manifest_vars = {
            "teamname": team_name_escaped,
            "subnet": str(team_subnet_cidr),
            "web_ip": str(team_network.next_host_address()),
            "proxy_ip": str(team_network.next_host_address()),
            "dns_ip": str(team_network.next_host_address()),
        }

        manifest = self.manifest_template.compile(manifest_vars)

        for service in team.services:

            service_name = f"{team_name_escaped}_{service.slug}"

            docker_service = DockerService(
                image=service.image,  # TODO: get image from service
                networks={
                    f"{team_name_escaped}_net": DockerNetworkSpec(
                        ipv4_address=service.ipAddress,
                    )
                },
                command=None,  # TODO: might need a custom command for additional setup, like setting up scripts or variables inside the container
                container_name=service_name
            )

            manifest.services[service_name] = docker_service

        self.compose.tear_down(manifest)

        result = self.team_collection.delete_one({"_id": ObjectId(team_id)})
