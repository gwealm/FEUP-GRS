from dataclasses import dataclass, field

from .models import *


@dataclass
class DockerComposeManifest:
    """
    Representation of a docker-compose.yaml manifest file.
    """

    version: float = 3.8
    services: dict = field(default_factory=dict)
    networks: dict = field(default_factory=dict)
    volumes: dict = field(default_factory=dict)
    secrets: dict = field(default_factory=dict)
    configs: dict = field(default_factory=dict)


class DockerComposeManifestTemplate:
    """
    Representation of a docker-compose.yaml manifest file template. This file is populated with given values to generate a concrete manifest.
    """

    def __init__(self):
        pass

    def compile(self, values: dict) -> DockerComposeManifest:
        """_summary_

        Args:
            values (dict): _description_

        Returns:
            DockerComposeManifest: _description_
        """

        pass
