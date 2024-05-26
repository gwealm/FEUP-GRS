from fastapi import APIRouter, Depends, HTTPException
from ..db import Database, Organization
from ..dependencies import get_db

router = APIRouter()

@router.post("/org/")
async def create_org(db: Database = Depends(get_db)):
    """
    Create a new organization.
    """
    org_id = db.get_next_org_id()
    org = Organization(id=org_id, name=f"Organization {org_id}", teams=[])
    db.create_org(org)
    return {"message": "Organization created", "organization_id": org_id}

@router.get("/org/{org_id}/teams")
async def get_teams(org_id: int, db: Database = Depends(get_db)):
    """
    Get all teams of the organization.
    """
    org = db.get_org(org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org.teams
