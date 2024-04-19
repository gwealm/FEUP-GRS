"""
Useful traits shared by multiple Compose configuration blocks.
"""

from abc import ABC
from typing import Optional


class HasLabels(ABC):
    """
    Abstract class that provides labels to subclasses.
    """

    labels: Optional[dict[str, str] | list[str]]
    """
    Docker labels attached to this object.
    """

    def __init__(self) -> None:
        super().__init__()
        self.labels = None


class CanBeExternal(ABC):
    """
    Abstract class that provides an external key to subclasses.
    """

    external: Optional[bool]
    """
    Whether this docker object was defined outside of this Compose file.
    
    Docker Compose will raise an error if it does not exist.
    """

    def __init__(self) -> None:
        super().__init__()
        self.external = None
