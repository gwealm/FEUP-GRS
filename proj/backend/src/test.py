from engine.docker.compose.handler import DockerComposeManifestHandler
from engine.docker.compose import DockerCompose

handler = DockerComposeManifestHandler()
compose = DockerCompose()

manifest_template = handler.load("../templates/docker-compose.yaml")

manifest = manifest_template.compile()

if compose.is_available():
    print("docker compose is available")
    compose.provision(manifest)
    print("docker compose project provisioned")
    compose.tear_down(manifest)
    print("docker compose project torn down")
