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
from engine.docker.compose.manifest import Manifest
from engine.docker.compose.models.network import IPAM as DockerIPAM
from engine.docker.compose.models.network import IPAMConfig as DockerIPAMConfig
from engine.docker.compose.models.network import Network as DockerNetwork
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

        team_network = Network(f"{team_spec.name}-network", cidr=team_subnet_cidr)

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

        team_spec_data = team_spec.model_dump()

        team_services_ids = team_spec_data['services']
        del team_spec_data['services']

        services: dict[str, DockerService] = {}
        team_services = []

        # Deploy services when a team is created
        for team_service_id in team_services_ids:

            service = self.get_service(team_service_id)

            service_address = team_network.next_host_address()

            # TODO: these should be handled by model converters
            docker_service = DockerService(
                image="",  # TODO: get image from service
                networks={
                    team_docker_network.name: DockerNetworkSpec(
                        ipv4_address=str(service_address),
                    )
                },
                command=None,  # TODO: might need a custom command for additional setup, like setting up scripts or variables inside the container
            )

            services[service.name] = docker_service
            team_services.append({"ref": DBRef(collection='services', id=team_service_id), "deployed_at": datetime.now(), "ip_address": str(service_address)})

        result = self.team_collection.insert_one(
            {
                **team_spec_data,
                "services": team_services,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now(),
            }
        )

        manifest = Manifest(
            services=services,
            networks={team_docker_network.name: team_docker_network},
        )

        team = self.get_team(result.inserted_id)

        return team

        # TODO: configure router, routes, DNS, etc etc

    def delete_team(self, team_id: int):
        """Remove a team from an existing organization."""

        # TODO: tear down team services.

        result = self.team_collection.delete_one({"_id": ObjectId(team_id)})
