from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from engine.docker.compose import DockerCompose
from engine.docker.compose.handler import DockerComposeManifestHandler

from dotenv import load_dotenv

from api.routers import team, services


@asynccontextmanager
async def lifespan(app: FastAPI):

    load_dotenv()

    compose = DockerCompose()
    handler = DockerComposeManifestHandler()

    manifest_template = handler.load("./templates/org-router.yml")

    # TODO: make these configurable, env vars?
    manifest = manifest_template.compile(
        {
            "orgname": os.getenv("ORG_NAME"),
            "subnet": os.getenv("ORG_SUBNET"),
            "router_ip": os.getenv("ORG_MAIN_ROUTER_IP_ADDR"),
            "project_base_path": os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "templates"
            ),
        }
    )

    print(handler.dump(manifest))

    compose.provision(manifest)

    # run the app
    yield

    compose.tear_down(manifest)


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(team.router)
app.include_router(services.router)


@app.get("/")
async def root():
    return {"message": "Hello GRS!"}
