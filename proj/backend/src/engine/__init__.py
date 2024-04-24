"""
Code related to a deployment engine for network configurations made in the application.
"""

from abc import ABC, abstractmethod
from .converter import Converter

from .models import Deployment


class Engine(ABC):
    """
    An engine is an object that can receive a deployment configuration and deploys it

    This class is abstract and should not be used. Instead use the specific deployment engines provided.
    """

    def __init__(self, name: str):
        self.name = name
        self.converters: dict[type[Converter], type[Converter]] = {}

    @abstractmethod
    def deploy(self, config: Deployment) -> None:
        """
        Deploys the specified deployment configuration.
        """

    @abstractmethod
    def is_available(self) -> bool:
        """
        
        """
