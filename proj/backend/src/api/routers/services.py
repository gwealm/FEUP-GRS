from fastapi import APIRouter, Depends, HTTPException
from ..db import Database
from ..dependencies import get_db
from functools import reduce

router = APIRouter(prefix="/services")


@router.get("/")
async def get_services(db: Database = Depends(get_db)):
    """
    Return existing services
    """

    services = db.get_services()

    grouped_services = {}
    for service in services:
        if service.tag not in grouped_services:
            grouped_services[service.tag] = []

        grouped_services[service.tag].append(service)

    return grouped_services


@router.get("/{service_id}")
async def get_team(service_id: str, db: Database = Depends(get_db)):
    """
    Get information about a specific team.
    """

    team = db.get_service(service_id)

    if not team:
        raise HTTPException(status_code=404, detail="Service not found")

    return team
