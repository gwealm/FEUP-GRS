"""
Classes related to volume configuration specifications inside a docker-compose.yaml file.
"""

from typing import Optional
from dataclasses import dataclass

from .traits import HasLabels, CanBeExternal, GenerateConfig
from .types import Value


@dataclass
class DriverOptions(dict[str, Value]):
    """
    Representation of driver-specific options for a given volume.
    """


@dataclass(kw_only=True, frozen=True, slots=True)
class Volume(HasLabels, CanBeExternal, GenerateConfig):
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

    @staticmethod
    def parse(volume_name: str, volume_spec: dict[str, Value]) -> "Volume":
        """Parses a dictionary representing a volume specification into a Volume object.

        Args:
            volume_name (str): the name of the volume as specified in the Compose file.
            volume_spec (dict[str, Value]): configuration values for this volume.

        Returns:
            Volume: an object representing the Volume specification
        """

        name = volume_spec.get("name", volume_name)
        driver = volume_spec.get("driver", None)
        driver_opts: DriverOptions = volume_spec.get("driver_opts", None)

        return Volume(
            name=name,
            driver=driver,
            driver_opts=driver_opts,
        )
