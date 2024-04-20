"""
Classes related to Docker Swarm configuration block inside a docker-compose.yaml file.
"""

from dataclasses import dataclass
from typing import Optional

from .traits import CanBeExternal
from .types import Value


@dataclass
class DriverOptions(dict[str, str | int | float | bool]):
    """
    Representation of driver-specific options for a given Config driver.
    """


@dataclass(kw_only=True, frozen=True, slots=True)
class Config(CanBeExternal):
    """
    A configuration object for Docker Swarm.
    """

    file: Optional[str]
    """
    The config is created with the contents of the file at the specified path.
    """

    name: str
    """
    The name of this config object. If not provided, will use the name in the Compose file.
    """

    # TODO: create separate classes for this, taking driver_opts into account
    driver: Optional[str]

    driver_opts: Optional[DriverOptions]
    """
    Driver specific options used by this Configuration object's driver.
    """

    template_driver: Optional[str]
    """
    The name of the templating driver to use,
    which controls whether and how to evaluate the secret payload as a template
    """

    @staticmethod
    def parse(config_name: str, config_spec: dict[str, Value]) -> "Config":
        """Parses a dictionary representing a config specification into a Config object.

        Args:
            config_spec (dict[str, Value]): configuration values for this config object.

        Returns:
            Config: the parsed config object.
        """

        file = config_spec.get("file", None)
        name = config_spec.get("name", config_name)
        driver = config_spec.get("driver", None)
        driver_opts = config_spec.get("driver_opts", None)
        template_driver = config_spec.get("template_driver", None)

        return Config(
            file=file,
            name=name,
            driver=driver,
            driver_opts=driver_opts,
            template_driver=template_driver,
        )
