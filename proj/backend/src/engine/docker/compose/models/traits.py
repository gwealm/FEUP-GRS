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


class GenerateConfig(ABC):
    """
    Abstract class that provides the ability to generate configuration from models.
    """

    def _filter_attr(self, attr):
        return not attr.startswith("_") and attr not in ('parse', 'to_dict')
    def to_dict(self):
        """ """

        config = {}

        attrs = [attr for attr in dir(self) if self._filter_attr(attr)]

        for attr in attrs:
            value = getattr(self, attr)

            if value is not None:

                if isinstance(value, GenerateConfig):
                    config[attr] = value.to_dict()
                else:
                    config[attr] = value

        return config
