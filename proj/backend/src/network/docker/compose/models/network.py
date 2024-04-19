"""
Classes related to network configuration specifications inside a docker-compose.yaml file.
"""

from dataclasses import dataclass
from typing import Optional

from .traits import HasLabels, CanBeExternal


@dataclass
class DriverOptions(dict[str, str | int | float | bool]):
    """
    Representation of driver-specific options for a given network.
    """


@dataclass(kw_only=True, frozen=True)
class IPAMConfig:
    """
    Configuration for an IPAM block.
    """

    subnet: str
    """
    The subnet belonging to this network, in CIDR notation.
    """

    gateway: Optional[str]
    """
    The default gateway for this IPAM address space.
    """


@dataclass(kw_only=True, frozen=True)
class IPAM:
    """
    IP Address Management options for a given network.
    """

    driver: Optional[str]
    """
    Custom IPAM driver to use instead of the default.
    """

    config: Optional[list[IPAMConfig]]
    """
    IPAM configuration for this network.
    """


@dataclass(kw_only=True, frozen=True, slots=True)
class Network(HasLabels, CanBeExternal):
    """
    Representation of a docker-compose.yaml network mapping block.
    """

    # TODO: create separate classes for this, taking driver_opts into account
    driver: Optional[str]
    """
    The driver used by the Docker Engine to create and manage this network.
    """

    driver_opts: Optional[DriverOptions]
    """
    The driver-specific options used by the Docker Engine
    when delegating network requests to the specified driver.
    """

    attachable: Optional[bool]
    """
    Specifies whether standalone containers can be attached to this network.

    Only works when using the 'overlay' driver.
    """

    enable_ipv6: Optional[bool]
    """
    Enable IPv6 networking.

    Only supported in Compose File Version 2.
    """

    ipam: Optional[IPAM]
    """
    IP Address Management options for this network.
    """

    internal: Optional[bool]
    """
    By default, Docker also connects a bridge network to it to provide external connectivity.
    If you want to create an externally isolated overlay network, you can set this option to true.
    """

    name: Optional[str]
    """
    The name of this network. If it is not provided, it defaults to the name of the network in the Compose File.
    """
