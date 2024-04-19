"""
Classes related to volume configuration specifications inside a docker-compose.yaml file.
"""

from typing import Optional
from dataclasses import dataclass

from network.docker.compose.models.traits import HasLabels, CanBeExternal


@dataclass
class DriverOptions(dict[str, str | int | float | bool]):
    """
    Representation of driver-specific options for a given volume.
    """


@dataclass(kw_only=True, frozen=True, slots=True)
class Volume(HasLabels, CanBeExternal):
    """
    Representation of a docker-compose.yaml volume mapping block.
    """

    name: str
    """
    The name of this volume.
    If not provided, will default to the volume id as specified in the docker-compose.yaml file.
    """

    # TODO: create separate classes for this, taking driver_opts into account
    driver: Optional[str]
    """
    The driver used by the Docker Engine to create and manage this volume.
    """

    driver_opts: Optional[DriverOptions]
    """
    The driver-specific options used by the Docker Engine
    when delegating volume requests to the specified driver.
    """
