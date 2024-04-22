"""
Classes related to network configuration specifications inside a docker-compose.yaml file.
"""

from dataclasses import dataclass
from typing import Optional

from .traits import HasLabels, CanBeExternal
from .types import Value

from ....models.network import NetworkConverter, Network as AppNetwork


@dataclass
class DriverOptions(dict[str, Value]):
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

    gateway: Optional[str] = None
    """
    The default gateway for this IPAM address space.
    """

    @staticmethod
    def parse(ipam_config_spec: dict[str, Value]) -> "IPAMConfig":
        """Parses a dictionary representing an IPAM Config specification into an IPAM Config object.

        Args:
            IPAM_spec (dict[str, Value]): configuration values for this IPAM Config object.

        Returns:
            IPAM: an object representing the IPAM Config specification
        """

        subnet = ipam_config_spec.get("subnet")
        gateway = ipam_config_spec.get("gateway", None)

        return IPAMConfig(subnet=subnet, gateway=gateway)


@dataclass(kw_only=True, frozen=True)
class IPAM:
    """
    IP Address Management options for a given network.
    """

    driver: Optional[str] = None
    """
    Custom IPAM driver to use instead of the default.
    """

    config: Optional[list[IPAMConfig]] = None
    """
    IPAM configuration for this network.
    """

    @staticmethod
    def parse(ipam_spec: dict[str, Value]) -> "IPAM":
        """Parses a dictionary representing an IPAM specification into an IPAM object.

        Args:
            IPAM_spec (dict[str, Value]): configuration values for this IPAM object.

        Returns:
            IPAM: an object representing the IPAM specification
        """

        driver = ipam_spec.get("driver", None)

        config: Optional[list[IPAMConfig]] = None
        if "config" in ipam_spec:
            config = []

            for config_spec in ipam_spec["config"]:
                config.append(IPAMConfig.parse(config_spec))

        return IPAM(driver=driver, config=config)


@dataclass(kw_only=True, frozen=True, slots=True)
class Network(HasLabels, CanBeExternal):
    """
    Representation of a docker-compose.yaml network mapping block.
    """

    # TODO: create separate classes for this, taking driver_opts into account
    driver: Optional[str] = None
    """
    The driver used by the Docker Engine to create and manage this network.
    """

    driver_opts: Optional[DriverOptions] = None
    """
    The driver-specific options used by the Docker Engine
    when delegating network requests to the specified driver.
    """

    attachable: Optional[bool] = None
    """
    Specifies whether standalone containers can be attached to this network.

    Only works when using the 'overlay' driver.
    """

    enable_ipv6: Optional[bool] = None
    """
    Enable IPv6 networking.

    Only supported in Compose File Version 2.
    """

    ipam: Optional[IPAM] = None
    """
    IP Address Management options for this network.
    """

    internal: Optional[bool] = None
    """
    By default, Docker also connects a bridge network to it to provide external connectivity.
    If you want to create an externally isolated overlay network, you can set this option to true.
    """

    name: str
    """
    The name of this network. If it is not provided, it defaults to the name of the network in the Compose File.
    """

    @staticmethod
    def parse(network_name: str, network_spec: dict[str, Value]) -> "Network":
        """Parses a dictionary representing a network specification into a Network object.

        Args:
            network_name (str): the name of the network as specified in the Compose file.
            network_spec (dict[str, Value]): configuration values for this network.

        Returns:
            Network: an object representing the network specification
        """

        name = network_spec.get("name", network_name)
        internal = network_spec.get("internal", None)
        enable_ipv6 = network_spec.get("enable_ipv6", None)
        attachable = network_spec.get("attachable", None)
        driver = network_spec.get("driver", None)
        driver_opts: DriverOptions = network_spec.get("driver_opts", None)

        ipam: Optional[IPAM] = None
        if "ipam" in network_spec:
            ipam = IPAM.parse(network_spec["ipam"])

        return Network(
            name=name,
            internal=internal,
            enable_ipv6=enable_ipv6,
            attachable=attachable,
            driver=driver,
            driver_opts=driver_opts,
            ipam=ipam,
        )


class DockerNetworkConverter(NetworkConverter[Network]):
    """
    Allows converting from a Network-like, engine-specific class to the Network class,
    which can be interpreted by the application
    """

    def convert_to(self, model: Network) -> AppNetwork:
        """
        Allows converting from type T to type F
        """

    def convert_from(self, model: AppNetwork) -> Network:
        """
        Allows converting from type F to type T
        """
