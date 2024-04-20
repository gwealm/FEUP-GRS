"""_summary_
"""

import yaml
from yaml import Loader

from .manifest import ManifestTemplate, Manifest


class DockerComposeManifestHandler:
    """
    Loads a docker-compose.yaml manifest file.
    """

    def __init__(self):
        pass

    def load(self, path: str) -> ManifestTemplate:
        """Loads a docker-compose.yaml manifest file and

        returns a DockerComposeManifestTemplate object.

        Args:
            path (str): the path to the docker-compose.yaml manifest file

        Returns:
            ManifestTemplate: An object which can generate a concrete manifest.
        """

        with open(path, "r", encoding="utf-8") as f:
            manifest_str = f.read()

            manifest = ManifestTemplate(manifest_str)

            return manifest

    def dump(self, manifest: Manifest):
        pass
