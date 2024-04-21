"""
"""

from typing import TypeVar

from ..converter import Converter


from .host import Host

class Router(Host):
    """"""

T = TypeVar("T")

class RouterConverter(Converter[T, Router]):
    """
    Allows converting from a a Router-like, engine-specific class to the Router class,
    which can be interpreted by the application
    """