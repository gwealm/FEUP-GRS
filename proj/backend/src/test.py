from engine.docker.compose.loader import DockerComposeManifestHandler

import pprint

handler = DockerComposeManifestHandler()

manifest_template = handler.load("../templates/docker-compose.yaml")

pprint.pprint(manifest_template.compile({"EXAMPLE_DB": "example"}))