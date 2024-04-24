from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routers import organization, team

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(organization.router)
app.include_router(team.router)

@app.get("/")
async def root():
    return {"message": "Hello GRS!"}