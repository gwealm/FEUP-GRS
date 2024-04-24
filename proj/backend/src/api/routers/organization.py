from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from .team import Team  # Importing Team model from a file named team.py

router = APIRouter()

class Organization(BaseModel):
    """
    Represents an organization (list of teams).
    
    Attributes:
        teams (List[Team]): A list of Team objects representing the organization's teams.
    """
    teams: List[Team]


@router.get("/org/")
async def create_org():
    """
    Create a new organization.
    Note: Since there can only be one organization, this endpoint might return an error if the organization already exists.
    """

@router.put("/org/{service_name}")
async def add_service(service_name: str):
    """
    Add a new service to the organization.
    
    Args:
        service_name (str): The name of the service to add to the organization.
    """


@router.delete("/org/{service_name}")
async def remove_service(service_name: str):
    """
    Remove a service from the organization.
    
    Args:
        service_name (str): The name of the service to remove from the organization.
    """
