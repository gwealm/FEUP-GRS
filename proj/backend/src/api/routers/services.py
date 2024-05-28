from fastapi import APIRouter, Depends, HTTPException
from ..db import Database
from ..dependencies import get_db

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

@router.get("/default")
async def get_default_services(db: Database = Depends(get_db)):
    """
    Return default services
    """

    services = db.manifest_template.compile({
            "teamname": 0,
            "subnet": 0,
            "web_ip": 0,
            "proxy_ip": 0,
            "dns_ip": 0,
        }).services

    return list(map(lambda s: {"label": s.labels['service.label'], "description": s.labels['service.description']}, services.values()))

@router.get("/{service_id}")
async def get_team(service_id: str, db: Database = Depends(get_db)):
    """
    Get information about a specific team.
    """

    team = db.get_service(service_id)

    if not team:
        raise HTTPException(status_code=404, detail="Service not found")

    return team
