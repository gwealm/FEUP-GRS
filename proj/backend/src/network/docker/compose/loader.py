"""_summary_
"""

import yaml
from yaml import Loader

from .manifest import DockerComposeManifestTemplate, DockerComposeManifest


class DockerComposeManifestLoader:
    """
    Loads a docker-compose.yaml manifest file.
    """

    def __init__(self):
        pass

    def load(self, path: str) -> DockerComposeManifestTemplate:

        with open(path, "r", encoding="utf-8") as f:
            manifest_str = f.read()

            manifest_yaml = yaml.load(manifest_str, Loader=Loader)

            # TODO: parse object representation

            manifest = DockerComposeManifestTemplate()

    def dump(self, manifest: DockerComposeManifest):
        pass
