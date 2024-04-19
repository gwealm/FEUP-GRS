"""_summary_
"""

import yaml
from yaml import Loader

from .manifest import DockerComposeManifestTemplate, DockerComposeManifest


class DockerComposeManifestHandler:
    """
    Loads a docker-compose.yaml manifest file.
    """

    def __init__(self):
        pass

    def load(self, path: str) -> DockerComposeManifestTemplate:
        """Loads a docker-compose.yaml manifest file and

        returns a DockerComposeManifestTemplate object.

        Args:
            path (str): the path to the docker-compose.yaml manifest file

        Returns:
            DockerComposeManifestTemplate: An object which can generate a concrete manifest.
        """

        with open(path, "r", encoding="utf-8") as f:
            manifest_str = f.read()

            manifest = DockerComposeManifestTemplate(manifest_str)

            return manifest

    def dump(self, manifest: DockerComposeManifest):
        pass
