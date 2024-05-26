from fastapi import APIRouter, Depends, HTTPException
from ..db import Database, Team, Service
from ..dependencies import get_db

router = APIRouter()


@router.get("/org/{org_id}/team/{team_id}")
async def get_team(org_id: int, team_id: int, db: Database = Depends(get_db)):
    """
    Get information about a specific team.
    """
    org = db.get_org(org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    for team in org.teams:
        if team.id == team_id:
            return team
    raise HTTPException(status_code=404, detail="Team not found")


@router.post("/org/{org_id}/team/")
async def create_team(org_id: int, team: Team, db: Database = Depends(get_db)):
    """
    Create a new team in the organization.
    """
    db.create_team(org_id, team)
    return {"message": "Team created successfully"}


@router.delete("/org/{org_id}/team/{team_id}")
async def delete_team(org_id: int, team_id: int, db: Database = Depends(get_db)):
    """
    Delete a team from the organization.
    """
    db.delete_team(org_id, team_id)
    return {"message": "Team deleted successfully"}


@router.get("/org/{org_id}/team/{team_id}/services")
async def get_team_services(org_id: int, team_id: int, db: Database = Depends(get_db)):
    """
    Get services of a specific team.
    """
    org = db.get_org(org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    for team in org.teams:
        if team.id == team_id:
            return team.services
    raise HTTPException(status_code=404, detail="Team not found")


@router.put("/org/{org_id}/team/{team_id}/service/{service_name}/deploy")
async def deploy_service(org_id: int, team_id: int, service_name: str, db: Database = Depends(get_db)):
    """
    Deploy a new service for a team.
    """
    org = db.get_org(org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    for team in org.teams:
        if team.id == team_id:
            service_id = len(team.services) + 1
            service = Service(id=service_id, name=service_name)
            db.deploy_service(org_id, team_id, service)
            return {"message": f"Service {service_name} deployed successfully"}
    raise HTTPException(status_code=404, detail="Team not found")


@router.put("/org/{org_id}/team/{team_id}/service/{service_name}/stop")
async def stop_service(org_id: int, team_id: int, service_name: str, db: Database = Depends(get_db)):
    """
    Stop a service of a team.
    """
    db.stop_service(org_id, team_id, service_name)
    return {"message": f"Service {service_name} stopped successfully"}


@router.put("/org/{org_id}/team/{team_id}/service/{service_name}/start")
async def start_service(org_id: int, team_id: int, service_name: str, db: Database = Depends(get_db)):
    """
    Start a service for a team.
    """
    db.start_service(org_id, team_id, service_name)
    return {"message": f"Service {service_name} started successfully"}
