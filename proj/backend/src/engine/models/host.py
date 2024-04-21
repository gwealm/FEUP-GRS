"""_summary_
"""

from typing import TypeVar

from ..converter import Converter


class Host:
    """
    """


T = TypeVar("T")

class HostConverter(Converter[T, Host]):
    """
    Allows converting from an Host-like, engine-specific class to the Host class,
    which can be interpreted by the application
    """
