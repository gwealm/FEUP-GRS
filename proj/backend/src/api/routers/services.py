from fastapi import APIRouter, Depends
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
