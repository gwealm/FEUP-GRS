"""
Classes related to Docker Swarm configuration block inside a docker-compose.yaml file.
"""

from dataclasses import dataclass
from typing import Optional

from .traits import CanBeExternal


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

    name: Optional[str]
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
