from typing import List, Dict
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class Service(BaseModel):
    """
    Represents a service with a name and optional tags.
    
    Attributes:
        service_name (str): The name of the service.
        tags (Dict[str, str] | None): Optional tags associated with the service.
    """
    service_name: str
    configs: Dict[str, str] | None

class Team(BaseModel):
    """
    Represents a team with a name and a list of services.
    
    Attributes:
        team_name (str): The name of the team.
        services (List[Service]): A list of Service objects representing the team's services.
    """
    team_name: str
    services: List[Service]


@router.post("/team/")
async def create_team(team: Team):
    """
    Create a new team.
    
    Args:
        team (Team): The team object containing the team name and services.
    """


@router.get("/team/{team_name}")
async def get_team(team_name: str):
    """
    Retrieve information about a specific team.
    
    Args:
        team_name (str): The name of the team to retrieve information for.
    """


@router.delete("/team/{team_name}")
async def delete_team(team_name: str):
    """
    Delete a team.
    
    Args:
        team_name (str): The name of the team to delete.
    """

@router.put("/team/{team_name}/service/{service_name}")
async def add_service(team_name: str, service_name: str):
    """
    Add a service to a team.
    
    Args:
        team_name (str): The name of the team to which the service will be added.
        service_name (str): The name of the service to add.
    """


@router.delete("/team/{team_name}/service/{service_name}")
async def remove_service(team_name: str, service_name: str):
    """
    Remove a service from a team.
    
    Args:
        team_name (str): The name of the team from which the service will be removed.
        service_name (str): The name of the service to remove.
    """

@router.put("/team/{team_name}/service/{service_name}/dns")
async def add_dns_entry(team_name: str, service_name: str, dns_entry: str):
    """
    Add a DNS entry to a service belonging to a team.
    
    Args:
        team_name (str): The name of the team that owns the service.
        service_name (str): The name of the service to which the DNS entry will be added.
        dns_entry (str): The DNS entry to add to the service.
    """


@router.delete("/team/{team_name}/service/{service_name}/dns")
async def remove_dns_entry(team_name: str, service_name: str, dns_entry: str):
    """
    Remove a DNS entry from a service belonging to a team.
    
    Args:
        team_name (str): The name of the team that owns the service.
        service_name (str): The name of the service from which the DNS entry will be removed.
        dns_entry (str): The DNS entry to remove from the service.
    """
