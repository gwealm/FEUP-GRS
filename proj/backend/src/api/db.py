from typing import List, Optional
from datetime import datetime
import os

from pymongo import MongoClient
from bson.objectid import ObjectId
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
class TeamSpec(BaseModel):
    """Model representing a team."""

    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    cidr: str
    services: List[str]
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

    def get_team(self, team_id: int) -> Optional[TeamSpec]:
        """Get a team by id."""

        team = self.team_collection.find_one(ObjectId(team_id))

        if not team:
            return None

        team["id"] = str(team["_id"])
        del team["_id"]

        return TeamSpec(**team)

    def create_team(self, team_spec: TeamSpec):
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

        services: dict[str, DockerService] = {}

        # Deploy services when a team is created
        for teamServiceId in team_spec.services:

            service = self.get_service(teamServiceId)
            print(teamServiceId, service, team_spec.services)

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

            services[service.name] = dockerService

        team = self.team_collection.insert_one(
            {
                **team_spec.model_dump(),
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        )

        manifest = Manifest(
            services=services,
            networks={team_docker_network.name: team_docker_network},
        )

        print(manifest)
        print(team)

        # TODO: configure router, routes, DNS, etc etc

    def delete_team(self, team_id: int):
        """Remove a team from an existing organization."""

        team = self.get_team(team_id)

        # TODO: tear down team services.

        self.team_collection.delete_one({"_id": team_id})

    def deploy_service(self, team_id: int, service: Service):
        """Deploy a new service for a team."""
        pass

    def stop_service(self, org_id: int, team_id: int, service_name: str):
        """Stop a service of a team."""
        pass

    def start_service(self, org_id: int, team_id: int, service_name: str):
        """Start a service for a team."""
        pass
