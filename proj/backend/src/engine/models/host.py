"""_summary_
"""

from typing import TypeVar

from ..converter import Converter


class Host:
    """ """

    image: str
    """The image to deploy on this host."""

    name: str
    """The name of this host."""

    def __init__(self, name: str, image: str):
        self.name = name
        self.image = image

T = TypeVar("T")


class HostConverter(Converter[T, Host]):
    """
    Allows converting from an Host-like, engine-specific class to the Host class,
    which can be interpreted by the application
    """
