"""
Classes related to network configuration specifications inside a docker-compose.yaml file.
"""

from dataclasses import dataclass
from typing import Optional

from .traits import CanBeExternal, GenerateConfig
from .types import Value


@dataclass
class Secret(CanBeExternal, GenerateConfig):
    """
    A secrets object for Docker Swarm.
    """

    file: Optional[str]
    """
    The config is created with the contents of the file at the specified path.
    """

    name: str
    """
    The name of this config object. If not provided, will use the name in the Compose file.
    """

    template_driver: Optional[str]
    """
    The name of the templating driver to use,
    which controls whether and how to evaluate the secret payload as a template
    """

    @staticmethod
    def parse(secret_name: str, secret_spec: dict[str, Value]) -> "Secret":
        """Parses a dictionary representing a secret specification into a Secret object.

        Args:
            secret_spec (dict[str, Value]): configuration values for this secret object.

        Returns:
            Secret: the parsed secret object.
        """

        file = secret_spec.get("file", None)
        name = secret_spec.get("name", secret_name)
        template_driver = secret_spec.get("template_driver", None)

        return Secret(file=file, name=name, template_driver=template_driver)
