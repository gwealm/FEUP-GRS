"""
"""

from typing import TypeVar

from ...converter import Converter
from .address import IPAddress, CIDR
from ..host import Host


class Network:
    """ """

    def __init__(self, name: str, cidr: CIDR):
        """ """

        self.name = name
        self.cidr = cidr
        self.hosts: dict[IPAddress, Host] = {}
        self._next_host = self.cidr.base_address + 1

    def next_host_address(self) -> IPAddress:
        """_summary_

        Returns:
            IPAddress: _description_
        """

        next_host = self._next_host
        self._next_host = next_host + 1

        return next_host

    def add_host(self, host: Host, address: IPAddress):
        """ """

        self.hosts[address] = host


T = TypeVar("T")


class NetworkConverter(Converter[T, Network]):
    """
    Allows converting from a Network-like, engine-specific class to the Network class,
    which can be interpreted by the application
    """
