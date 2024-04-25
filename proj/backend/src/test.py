from engine.docker.compose.handler import DockerComposeManifestHandler

import pprint

handler = DockerComposeManifestHandler()

manifest_template = handler.load("../templates/docker-compose.yaml")

manifest = manifest_template.compile({"EXAMPLE_DB": "example"})

pprint.pprint(manifest)
pprint.pprint(handler.dump(manifest))
