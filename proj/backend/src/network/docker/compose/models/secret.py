"""
Classes related to network configuration specifications inside a docker-compose.yaml file.
"""

from dataclasses import dataclass
from typing import Optional

from .traits import CanBeExternal


@dataclass
class Secret(CanBeExternal):
    """
    A configuration object for Docker Swarm.
    """

    file: Optional[str]
    """
    The config is created with the contents of the file at the specified path.
    """

    name: Optional[str]
    """
    The name of this config object. If not provided, will use the name in the Compose file.
    """

    template_driver: Optional[str]
    """
    The name of the templating driver to use,
    which controls whether and how to evaluate the secret payload as a template
    """
