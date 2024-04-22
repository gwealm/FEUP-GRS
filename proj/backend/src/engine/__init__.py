"""
Code related to a deployment engine for network configurations made in the application.
"""

from abc import ABC, abstractmethod
from typing import Any
from .converter import Converter


class Engine(ABC):
    """
    An engine is an object that can receive a deployment configuration and deploys it

    This class is abstract and should not be used. Instead use the specific deployment engines provided.
    """

    def __init__(self, name: str):
        self.name = name
        self.converters: dict[type[Converter], type[Converter]] = {}

    @abstractmethod
    def deploy(self, config: Any) -> None:
        """
        Deploys the specified deployment configuration.
        """
