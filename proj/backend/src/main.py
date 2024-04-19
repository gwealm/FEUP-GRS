from network.docker.compose.loader import DockerComposeManifestHandler
import pprint

handler = DockerComposeManifestHandler()

manifest_template = handler.load(
    "/home/naapperas/workspace/uni/4-ano/grs/proj/backend/templates/docker-compose.yaml"
)

pprint.pprint(manifest_template.compile())
