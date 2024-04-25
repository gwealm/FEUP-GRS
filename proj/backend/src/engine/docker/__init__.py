"""
Classes and methods related to a Docker deployment engine.
"""

from typing import Any
from .compose import DockerCompose
from .compose.models import *

from .. import Engine
from ..models.network import NetworkConverter


class Docker(Engine):
    """
    A deployment engine that configures a network using Docker.
    """

    def __init__(self, name: str):
        super().__init__(name)

        self.compose = DockerCompose()

        # TODO: improve this configuration
        self.converters = {NetworkConverter: DockerNetworkConverter}

    def deploy(self, config: Any) -> None:
        # TODO: implement this function

        manifest = None

        self.compose.provision(manifest)

    def is_available(self) -> bool:
        return self.compose.is_available()
