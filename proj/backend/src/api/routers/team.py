from fastapi import APIRouter, Depends, HTTPException
from ..db import Database, TeamSpec
from ..dependencies import get_db

router = APIRouter(prefix="/team")


@router.get("/{team_id}")
async def get_team(team_id: str, db: Database = Depends(get_db)):
    """
    Get information about a specific team.
    """

    team = db.get_team(team_id)

    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    return team


@router.post("/")
async def create_team(team_spec: TeamSpec, db: Database = Depends(get_db)):
    """
    Create a new team in the organization.
    """

    db.create_team(team_spec)

    return {"message": "Team created successfully"}


@router.delete("/{team_id}")
async def delete_team(team_id: str, db: Database = Depends(get_db)):
    """
    Delete a team from the organization.
    """

    db.delete_team(team_id)

    return {"message": "Team deleted successfully"}
