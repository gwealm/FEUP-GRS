"""
Classes and methods related to converting an engine-specific model into an app model.
"""

from abc import ABC, abstractmethod

from typing import TypeVar, Generic

T = TypeVar("T")
F = TypeVar("F")

class Converter(Generic[T, F], ABC):
    """
    Abstract class that allows converting from one type to another.
    """

    @abstractmethod
    def convert_to(self, model: T) -> F:
        """
        Allows converting from type T to type F
        """

    @abstractmethod
    def convert_from(self, model: F) -> T:
        """
        Allows converting from type F to type T
        """
