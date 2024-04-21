"""
"""

from typing import TypeVar

from ..converter import Converter

class Network:
    """
    """

T = TypeVar("T")

class NetworkConverter(Converter[T, Network]):
    """
    Allows converting from a Network-like, engine-specific class to the Network class,
    which can be interpreted by the application
    """
