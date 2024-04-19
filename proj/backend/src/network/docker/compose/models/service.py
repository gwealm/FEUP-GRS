"""
Classes related to service configuration specifications inside a docker-compose.yaml file.
"""

from typing import Optional, Literal
from dataclasses import dataclass, field

from .traits import HasLabels
from .types import Duration, ByteValue, Value


@dataclass
class BindProperties:
    """
    Properties for bind mounts.
    """

    propagation: str
    """
    The propagation mode used inside for the bind.
    """

    create_host_path: bool
    """
    Creates a directory at the source path on host if there is nothing present.
    """

    selinux: Literal["z", "Z"]
    """
    Enable SELinux relabeling on the volume.
    """

    @staticmethod
    def parse(bind_properties_spec: dict[str, Value]) -> "BindProperties":
        """Parses a dictionary representing a bind mount specification into a BindProperties object.

        Args:
            bind_properties_spec (dict[str, Value]): configuration values for this BindProperties object.

        Returns:
            BindProperties: an object representing the BindProperties specification
        """

        return BindProperties(
            propagation=bind_properties_spec.get("propagation"),
            create_host_path=bind_properties_spec.get("create_host_path"),
            selinux=bind_properties_spec.get("selinux"),
        )


@dataclass
class VolumeProperties:
    """
    Properties for volumes.
    """

    nocopy: bool
    """
    Flag to disable copying of data from a container when a volume is created.
    """

    subpath: str
    """
    Path inside a volume to mount instead of the volume root.
    """

    @staticmethod
    def parse(volume_properties_spec) -> "VolumeProperties":
        """Parses a dictionary representing a volume specification into a VolumeProperties object.

        Args:
            volume_properties_spec (dict[str, Value]): configuration values for this volume.

        Returns:
            VolumeProperties: an object representing the VolumeProperties specification
        """

        return VolumeProperties(
            nocopy=volume_properties_spec.get("nocopy"),
            subpath=volume_properties_spec.get("subpath"),
        )


@dataclass
class TMPFSProperties:
    """
    Properties for TMPFS volumes.
    """

    size: int | ByteValue
    """
    The size for the tmpfs mount in bytes
    """

    mode: int
    """
    The file mode for the tmpfs mount as Unix permission bits as an octal number
    """

    @staticmethod
    def parse(tmpfs_properties_spec: dict[str, Value]) -> "TMPFSProperties":
        """Parses a dictionary representing a TMPFS volume specification into a TMPFSProperties object.

        Args:
            tmpfs_properties_spec (dict[str, Value]): configuration values for this TMPFSProperties object.

        Returns:
            TMPFSProperties: an object representing the TMPFSProperties specification
        """

        return TMPFSProperties(
            size=tmpfs_properties_spec.get("size"),
            mode=tmpfs_properties_spec.get("mode"),
        )


@dataclass
class Volume:
    """
    Volume mounted on a container through a filesystem bind.
    """

    type: Literal["volume", "bind", "tmpfs", "npipe", "cluster"]
    """
    The type of this volume
    """

    source: str
    """
    The source of the mount, a path on the host for a bind mount, or the name of a volume
    """

    target: str
    """
    The path in the container where the volume is mounted.
    """

    read_only: Optional[bool] = None
    """
    Flag to set volume as read-only.
    """

    bind: Optional[BindProperties] = None
    """
    Additional properties for the bind mount
    """

    volume: Optional[VolumeProperties] = None
    """
    Additional properties for the volume mount.
    """

    tmpfs: Optional[TMPFSProperties] = None
    """
    Additional properties for the tmpfs mount.
    """

    consistency: Optional[str] = None
    """
    The consistency requirements for the the mount. Values are platform dependent.
    """

    @staticmethod
    def parse(volume_spec: dict[str, Value]) -> "Volume":
        """_summary_

        Args:
            volume_spec (dict[str, Value]): _description_

        Returns:
            Volume: _description_
        """

        source = volume_spec.get("source")
        target = volume_spec.get("target", source)
        read_only = volume_spec.get("read_only", None)

        if "bind" in volume_spec:
            bind = BindProperties.parse(volume_spec.get("bind"))
        else:
            bind = None

        if "read_only" in volume_spec:
            volume = VolumeProperties.parse(volume_spec.get("volume", {}))
        else:
            volume = None

        if "tmpfs" in volume_spec:
            tmpfs = TMPFSProperties.parse(volume_spec.get("tmpfs", {}))
        else:
            tmpfs = None

        consistency = volume_spec.get("consistency", None)

        return Volume(
            type=volume_spec.get("type"),
            source=source,
            target=target,
            read_only=read_only,
            bind=bind,
            volume=volume,
            tmpfs=tmpfs,
            consistency=consistency,
        )


@dataclass
class FailureRestartPolicy:
    """
    Policy applied when restarting a service container.
    """

    max_retries: Optional[int] = None
    """
    Max number of retries for terminated containers.
    """

    def __repr__(self) -> str:
        max_retries_str = "" if self.max_retries is not None else f":{self.max_retries}"

        return f"on-failure{max_retries_str}"


@dataclass
class PortSpec:
    """
    Specification o an exposed port.
    """

    name: str
    """
    A human readable name for the port.
    """

    target: int
    """
    The container port.
    """

    published: str
    """
    The published port. Can be set as a range.
    """

    app_protocol: Optional[str]
    """
    Hint to Compose about the application protocol that this port is used for.
    """

    host_ip: Optional[str] = field(default="0.0.0.0")
    """
    The IP address on the host to bind to.
    """

    protocol: Optional[str] = field(default="tcp")
    """
    The port protocol.
    """

    mode: Literal["host", "ingress"] = field(default="ingress")
    """
    The port mode.
    """

    @staticmethod
    def parse(port_name: str, port_spec: dict[str, Value]) -> "PortSpec":
        """Parses a dictionary representing a port specification into a PortSpec object.

        Args:
            port_spec (dict[str, Value]): configuration values for this PortSpec object.

        Returns:
            PortSpec: an object representing the PortSpec specification
        """

        return PortSpec(
            name=port_spec.get("name", port_name),
            target=port_spec.get("target"),
            published=port_spec.get("published"),
            app_protocol=port_spec.get("app_protocol"),
            host_ip=port_spec.get("host_ip", "0.0.0.0"),
            protocol=port_spec.get("protocol", "tcp"),
            mode=port_spec.get("mode", "ingress"),
        )


@dataclass
class NetworkSpec:
    """
    Configuration of network attachments for this service's container.
    """

    aliases: Optional[list[str]]
    """
    Declares alternative hostnames for the service on the network
    """

    ipv4_address: Optional[str]
    """
    Defines the IPv4 address for the service container on the network.
    """

    ipv6_address: Optional[str]
    """
    Defines the IPv6 address for the service container on the network if IPv6 networking is enabled.
    """

    link_local_ips: Optional[list[str]]
    """
    Specifies a list of link-local IPs.
    Link-local IPs are special IPs which belong to a well known subnet
    and are purely managed by the operator,
    usually dependent on the architecture where they are deployed.
    """

    mac_address: Optional[str]
    """
    Defines the MAC address for the service container on the network.
    """

    priority: Optional[int] = field(default=0)
    """
    Indicates in which order Compose connects the service’s containers to its networks.
    """

    @staticmethod
    def parse(network_spec: dict[str, Value]) -> "NetworkSpec":
        """Parses a dictionary representing a network specification into a NetworkSpec object.

        Args:
            network_spec (dict[str, Value]): configuration values for this NetworkSpec object.

        Returns:
            NetworkSpec: an object representing the NetworkSpec specification
        """

        return NetworkSpec(
            aliases=network_spec.get("aliases", None),
            ipv4_address=network_spec.get("ipv4_address", None),
            ipv6_address=network_spec.get("ipv6_address", None),
            link_local_ips=network_spec.get("link_local_ips", None),
            mac_address=network_spec.get("mac_address", None),
            priority=network_spec.get("priority", 0),
        )


@dataclass
class LoggingConfig:
    """
    Logging configuration for this service.
    """

    driver: str
    """
    Logging driver for this service. Values are platform specific.
    """

    options: dict[str, Value]
    """
    Driver specific options.
    """

    @staticmethod
    def parse(logging_config_spec: dict[str, Value]) -> "LoggingConfig":
        """Parses a dictionary representing a logging configuration into a LoggingConfig object.

        Args:
            logging_config_spec (dict[str, Value]): configuration values for this LoggingConfig object.

        Returns:
            LoggingConfig: an object representing the LoggingConfig specification
        """

        return LoggingConfig(
            driver=logging_config_spec.get("driver"),
            options=logging_config_spec.get("options", {}),
        )


@dataclass
class IPCService:
    """
    Represents another service's IPC namespace.
    """

    service: str

    def __repr__(self) -> str:
        return f"service:{self.service}"


@dataclass
class NetworkMode:
    """
    Represents another service's network.
    """

    service: str

    def __repr__(self) -> str:
        return f"service:{self.service}"


@dataclass
class HealthCheck:
    """
    Specification of how to perform an health check to this service's containers.
    """

    test: list[str] | str
    """
    Defines the command Compose runs to check container health
    """

    retries: int
    """
    """

    disable: Optional[bool]
    """
    Whether to disable any default health checks set by the image.
    """

    interval: Duration = field(default_factory=Duration.zero)
    """
    """

    timeout: Duration = field(default_factory=Duration.zero)
    """
    """

    start_period: Duration = field(default_factory=Duration.zero)
    """
    """

    @staticmethod
    def parse(health_check_spec: dict[str, Value]) -> "HealthCheck":

        return HealthCheck(
            test=health_check_spec.get("test"),
            retries=health_check_spec.get("retries", 0),
            disable=health_check_spec.get("disable", False),
            interval=Duration.from_string(health_check_spec.get("interval", "0s")),
            timeout=Duration.from_string(health_check_spec.get("timeout", "0s")),
            start_period=Duration.from_string(
                health_check_spec.get("start_period", "0s")
            ),
        )


@dataclass
class ExtensionsSpec:
    """
    Specification for service extensions
    """

    file: str
    """
    The location of a Compose configuration file defining that service.
    """

    service: str
    """
    Defines the name of the service being referenced as a base.
    """

    @staticmethod
    def parse(extensions_spec: dict[str, Value]) -> "ExtensionsSpec":
        """Parses a dictionary representing a extensions specification into a ExtensionsSpec object.

        Args:
            extensions_spec (dict[str, Value]): configuration values for this ExtensionsSpec object.

        Returns:
            ExtensionsSpec: an object representing the ExtensionsSpec specification
        """

        return ExtensionsSpec(
            file=extensions_spec.get("file"),
            service=extensions_spec.get("service"),
        )


@dataclass
class EnvFile:
    """
    Specification of an environment file to load.
    """

    path: str
    """
    The path to the environment file.
    """

    required: bool
    """
    Whether this file is required to exist.
    """

    @staticmethod
    def parse(env_file_spec: dict[str, Value]) -> "EnvFile":
        """Parses a dictionary representing an environment file into an EnvFile object.

        Args:
            env_file_spec (dict[str, Value]): configuration values for this EnvFile object.

        Returns:
            EnvFile: an object representing the EnvFile specification
        """

        return EnvFile(
            path=env_file_spec.get("path"),
            required=env_file_spec.get("required", False),
        )


@dataclass
class DevelopmentWatch:
    """
    Rule applied by Compose to monitor source code for changes.
    """

    action: Literal["rebuild", "sync", "sync+restart"]
    """
    Action to take when source code changes are detected.
    """

    path: str
    """
    Defines the path to source code.
    """

    ignore: Optional[list[str]]
    """
    Define a list of patterns for paths to ignore when source code changes are detected.
    """

    target: Optional[str]
    """
    Files within path with changes are synchronized with container filesystem,
    so that the latter is always running with up-to-date content.
    """

    @staticmethod
    def parse(development_watch_spec: dict[str, Value]) -> "DevelopmentWatch":
        """Parses a dictionary representing a development watch specification into a DevelopmentWatch object.

        Args:
            development_watch_spec (dict[str, Value]): configuration values for this DevelopmentWatch object.

        Returns:
            DevelopmentWatch: an object representing the DevelopmentWatch specification
        """

        return DevelopmentWatch(
            action=development_watch_spec.get("action"),
            path=development_watch_spec.get("path"),
            ignore=development_watch_spec.get("ignore", None),
            target=development_watch_spec.get("target", None),
        )


@dataclass
class Development:
    """
    Specifications of how to maintain a service in sync with source.
    """

    watch: list[DevelopmentWatch]
    """
    Defines a list of rules that control automatic service updates based on local file changes.
    """

    @staticmethod
    def parse(development_spec: dict[str, Value]) -> "Development":
        """Parses a dictionary representing a development specification into a Development object.

        Args:
            development_spec (dict[str, Value]): configuration values for this Development object.

        Returns:
            Development: an object representing the Development specification
        """

        return Development(
            watch=[
                DevelopmentWatch.parse(watch_spec)
                for watch_spec in development_spec.get("watch", [])
            ]
        )


@dataclass
class UpdateConfig:
    """
    Specifications for service updates.
    """

    parallelism: Optional[int]
    """
    The number of containers to update at a time.
    """

    delay: Optional[Duration] = field(default_factory=Duration.zero)
    """
    The time to wait between updating a group of containers.
    """

    failure_action: Optional[Literal["pause", "continue", "rollback"]] = field(
        default="pause"
    )
    """
    What to do if an update fails.
    """

    monitor: Optional[Duration] = field(default_factory=Duration.zero)
    """
    Duration after each task update to monitor for failure.
    """

    max_failure_ratio: Optional[float] = field(default=0)
    """
    Failure rate to tolerate during an update.
    """

    order: Optional[Literal["stop-first", "start-first"]] = field(default="stop-first")
    """
    Order of operations during updates.
    """

    @staticmethod
    def parse(update_config_spec: dict[str, Value]) -> "UpdateConfig":
        """Parses a dictionary representing an update configuration into an UpdateConfig object.

        Args:
            update_config_spec (dict[str, Value]): configuration values for this UpdateConfig object.

        Returns:
            UpdateConfig: an object representing the UpdateConfig specification
        """

        return UpdateConfig(
            parallelism=update_config_spec.get("parallelism"),
            delay=Duration.from_string(update_config_spec.get("delay", "0s")),
            failure_action=update_config_spec.get("failure_action"),
            monitor=Duration.from_string(update_config_spec.get("monitor", "0s")),
            max_failure_ratio=update_config_spec.get("max_failure_ratio"),
            order=update_config_spec.get("order"),
        )


@dataclass
class RollbackConfig:
    """
    Specifications for service update rollbacks.
    """

    parallelism: Optional[int]
    """
    The number of containers to rollback.
    """

    delay: Optional[Duration] = field(default_factory=Duration.zero)
    """
    The time to wait between each container group's rollback.
    """

    failure_action: Optional[Literal["pause", "continue"]] = field(default="pause")
    """
    What to do if a rollback fails.
    """

    monitor: Optional[Duration] = field(default_factory=Duration.zero)
    """
    Duration after each task rollback to monitor for failure.
    """

    max_failure_ratio: Optional[float] = field(default=0)
    """
    Failure rate to tolerate during a rollback.
    """

    order: Optional[Literal["stop-first", "start-first"]] = field(default="stop-first")
    """
    Order of operations during rollbacks.
    """

    @staticmethod
    def parse(rollback_config_spec: dict[str, Value]) -> "RollbackConfig":
        """Parses a dictionary representing a rollback configuration into a RollbackConfig object.

        Args:
            rollback_config_spec (dict[str, Value]): configuration values for this RollbackConfig object.

        Returns:
            RollbackConfig: an object representing the RollbackConfig specification
        """

        return RollbackConfig(
            parallelism=rollback_config_spec.get("parallelism"),
            delay=Duration.from_string(rollback_config_spec.get("delay", "0s")),
            failure_action=rollback_config_spec.get("failure_action"),
            monitor=Duration.from_string(rollback_config_spec.get("monitor", "0s")),
            max_failure_ratio=rollback_config_spec.get("max_failure_ratio"),
            order=rollback_config_spec.get("order"),
        )


@dataclass
class RestartPolicy:
    """
    Configurations for how to restart a container when it exits.
    """

    condition: Literal["none", "on-failure", "any"]
    """
    Defines the condition for restarting this container.
    """

    max_attempts: Optional[int]
    """
    Specifies the maximum number of attempts to restart the container.
    """

    delay: Optional[Duration] = field(default_factory=Duration.zero)
    """
    The time to wait before restarting the container.
    """

    window: Optional[Duration] = field(default_factory=Duration.zero)
    """
    How long to wait before deciding if a restart has succeeded
    """

    @staticmethod
    def parse(restart_policy_spec: dict[str, Value]) -> "RestartPolicy":
        """Parses a dictionary representing a restart policy specification into a RestartPolicy object.

        Args:
            restart_policy_spec (dict[str, Value]): configuration values for this RestartPolicy object.

        Returns:
            RestartPolicy: an object representing the RestartPolicy specification
        """

        return RestartPolicy(
            condition=restart_policy_spec.get("condition"),
            max_attempts=restart_policy_spec.get("max_attempts"),
            delay=Duration.from_string(restart_policy_spec.get("delay", "0s")),
            window=Duration.from_string(restart_policy_spec.get("window", "0s")),
        )


@dataclass
class Devices:
    """
    Specifications of the reservations of the devices a container can use.
    """

    capabilities: Optional[list[str | Literal["gpu", "tpu"]]]
    """
    List of devices to reserve.
    """

    driver: Optional[str]
    """
    The name of the device driver to use.
    """

    count: Optional[int | Literal["all"]]
    """
    Number of devices to reserve.
    """

    device_ids: Optional[list[str]]
    """
    Compose reserves devices with the specified IDs provided they satisfy the requested capabilities
    """

    options: Optional[dict[str, Value]]
    """
    Driver specific options.
    """

    @staticmethod
    def parse(devices_spec: dict[str, Value]) -> "Devices":
        """Parses a dictionary representing a devices specification into a Devices object.

        Args:
            devices_spec (dict[str, Value]): configuration values for this Devices object.

        Returns:
            Devices: an object representing the Devices specification
        """

        return Devices(
            capabilities=devices_spec.get("capabilities"),
            driver=devices_spec.get("driver"),
            count=devices_spec.get("count"),
            device_ids=devices_spec.get("device_ids"),
            options=devices_spec.get("options"),
        )


@dataclass
class ResourceSpec:
    """
    Specification for a platform's resource constraints.
    """

    cpus: Optional[str]
    """
    Configures a limit or reservation for how much of the available CPU resources,
    as number of cores.
    """

    memory: Optional[ByteValue]
    """
    Configures a limit or reservation on the amount of memory a container can allocate.
    """

    pids: Optional[int]
    """
    Tunes a container’s PIDs limit.
    """

    devices: Optional[list[Devices]]
    """
    Configures reservations of the devices a container can use
    """

    @staticmethod
    def parse(resource_spec_spec: dict[str, Value]) -> "ResourceSpec":
        """Parses a dictionary representing a resource specification into a ResourceSpec object.

        Args:
            resource_spec_spec (dict[str, Value]): configuration values for this ResourceSpec object.

        Returns:
            ResourceSpec: an object representing the ResourceSpec specification
        """

        return ResourceSpec(
            cpus=resource_spec_spec.get("cpus"),
            memory=ByteValue.from_string(resource_spec_spec.get("memory")),
            pids=resource_spec_spec.get("pids"),
            devices=[Devices.parse(d) for d in resource_spec_spec.get("devices", [])],
        )


@dataclass
class Resources:
    """
    Configures physical resource constraints for container to run on platform
    """

    limits: Optional[ResourceSpec]
    """
    The platform must prevent the container to allocate more
    """

    reservations: Optional[ResourceSpec]
    """
    The platform must guarantee the container can allocate at least the configured amount.
    """

    @staticmethod
    def parse(resources_spec: dict[str, Value]) -> "Resources":
        """Parses a dictionary representing a resources specification into a Resources object.

        Args:
            resources_spec (dict[str, Value]): configuration values for this Resources object.

        Returns:
            Resources: an object representing the Resources specification
        """

        return Resources(
            limits=ResourceSpec.parse(resources_spec.get("limits")),
            reservations=ResourceSpec.parse(resources_spec.get("reservations")),
        )


@dataclass
class Placement:
    """
    Specifies constraints and preferences for the platform
    to select a physical node to run service containers.
    """

    constraints: Optional[list[str] | dict[str, str]]
    """
    Defines a required property the platform's node must fulfill to run the service container.
    """

    preferences: Optional[list[str] | dict[str, str]]
    """
    Defines a required property the platform's node should fulfill to run the service container.
    """

    @staticmethod
    def parse(placement_spec: dict[str, Value]) -> "Placement":
        """Parses a dictionary representing a placement specification into a Placement object.

        Args:
            placement_spec (dict[str, Value]): configuration values for this Placement object.

        Returns:
            Placement: an object representing the Placement specification
        """

        return Placement(
            constraints=placement_spec.get("constraints", None),
            preferences=placement_spec.get("preferences", None),
        )


@dataclass
class Deployment(HasLabels):
    """
    Specifies deployment options for this service.
    """

    endpoint_mode: Literal["vip", "dnsrr"]
    """
    Specifies a service discovery method for external clients connecting to a service.
    """

    placement: Optional[Placement]
    """
    Specifies constraints and preferences for the platform
    to select a physical node to run service containers.
    """

    replicas: Optional[int]
    """
    Specifies the number of replicas to run the service container if the service is replicated.
    """

    resources: Optional[Resources]
    """
    Defines resource constraints for the service.
    """

    restart_policy: Optional[RestartPolicy]
    """
    Defines the policy for restarting the service.
    """

    rollback_config: Optional[RollbackConfig]
    """
    Configures how the service should be rollbacked in case of a failing update.
    """

    update_config: Optional[UpdateConfig]
    """
    Configures how the service should be updated.
    """

    mode: Literal["global", "replicated"] = field(default=Literal["replicated"])
    """
    Defines the replication model used to run the service on the platform
    """

    @staticmethod
    def parse(deployment_spec: dict[str, Value]) -> "Deployment":
        """ """

        endpoint_mode = deployment_spec.get("endpoint_mode")
        if endpoint_mode not in ["vip", "dnsrr"]:
            raise ValueError(f"Invalid endpoint_mode: {endpoint_mode}")

        deployment = Deployment(
            endpoint_mode=endpoint_mode,
            placement=Placement.parse(deployment_spec.get("placement")),
            replicas=deployment_spec.get("replicas"),
            resources=Resources.parse(deployment_spec.get("resources")),
            restart_policy=RestartPolicy.parse(deployment_spec.get("restart_policy")),
            rollback_config=RollbackConfig.parse(
                deployment_spec.get("rollback_config")
            ),
            update_config=UpdateConfig.parse(deployment_spec.get("update_config")),
            mode=deployment_spec.get("mode", "replicated"),
        )
        deployment.labels = (deployment_spec.get("labels", {}),)

        return deployment


@dataclass
class DependencyConfig:
    """
    Dependency configurations for a service.
    """

    restart: bool
    """
    When set to true Compose restarts this service after it updates the dependency services
    """

    condition: Literal[
        "service_started", "service_healthy", "service_completed_successfully"
    ]
    """
    Sets the condition under which dependency is considered satisfied
    """

    required: Optional[bool] = field(default=True)
    """
    When set to false Compose only warns you when the dependency service isn't started or available
    """

    @staticmethod
    def parse(dependency_config_spec: dict[str, Value]) -> "DependencyConfig":
        """Parses a dictionary representing a dependency configuration into a DependencyConfig object.

        Args:
            dependency_config_spec (dict[str, Value]): configuration values for this DependencyConfig object.

        Returns:
            DependencyConfig: an object representing the DependencyConfig specification
        """

        return DependencyConfig(
            restart=dependency_config_spec.get("restart"),
            condition=dependency_config_spec.get("condition"),
            required=dependency_config_spec.get("required"),
        )


@dataclass
class CredentialSpecFile:
    """
    Specifies a CredentialSpec inside a file
    """

    file: str
    """
    The path of the file containing the CredentialSpec
    """

    @staticmethod
    def parse(credential_spec_file_spec: dict[str, Value]) -> "CredentialSpecFile":
        """Parses a dictionary representing a credential specification file into a CredentialSpecFile object.

        Args:
            credential_spec_file_spec (dict[str, Value]): configuration values for this CredentialSpecFile object.

        Returns:
            CredentialSpecFile: an object representing the CredentialSpecFile specification
        """

        return CredentialSpecFile(
            file=credential_spec_file_spec.get("file"),
        )


@dataclass
class CredentialSpecRegistry:
    """
    Specifies a CredentialSpec inside a registry
    """

    registry: str
    """
    The path of the registry containing the CredentialSpec
    """

    @staticmethod
    def parse(
        credential_spec_registry_spec: dict[str, Value]
    ) -> "CredentialSpecRegistry":
        """Parses a dictionary representing a credential specification registry into a CredentialSpecRegistry object.

        Args:
            credential_spec_registry_spec (dict[str, Value]): configuration values for this CredentialSpecRegistry object.

        Returns:
            CredentialSpecRegistry: an object representing the CredentialSpecRegistry specification
        """

        return CredentialSpecRegistry(
            registry=credential_spec_registry_spec.get("registry"),
        )


@dataclass
class CredentialSpecConfig:
    """
    Specifies a CredentialSpec inside a config
    """

    config: str
    """
    The path of the config containing the CredentialSpec
    """

    @staticmethod
    def parse(credential_spec_config_spec: dict[str, Value]) -> "CredentialSpecConfig":
        """Parses a dictionary representing a credential specification config into a CredentialSpecConfig object.

        Args:
            credential_spec_config_spec (dict[str, Value]): configuration values for this CredentialSpecConfig object.

        Returns:
            CredentialSpecConfig: an object representing the CredentialSpecConfig specification
        """

        return CredentialSpecConfig(
            config=credential_spec_config_spec.get("config"),
        )


@dataclass
class BlockIOConfig:
    """
    Defines options related to block device IO operations by the service.
    """

    @dataclass
    class BPS:
        """
        Limit configuration in bytes/second
        """

        path: str
        """
        Defines the symbolic path to the affected device.
        """

        rate: int | ByteValue
        """
        Number of bytes per second.
        """

        @staticmethod
        def parse(bps_spec: dict[str, Value]) -> "BlockIOConfig.BPS":
            """Parses a dictionary representing a BPS configuration into a BPS object.

            Args:
                bps_spec (dict[str, Value]): configuration values for this BPS object.

            Returns:
                BlockIOConfig.BPS: an object representing the BPS specification
            """

            try:
                rate = int(bps_spec.get("rate"))
            except ValueError:
                rate = ByteValue.from_string(bps_spec.get("rate"))

            return BlockIOConfig.BPS(path=bps_spec.get("path"), rate=rate)

    @dataclass
    class IOPS:
        """
        Limit configuration in operations/second
        """

        path: str
        """
        Defines the symbolic path to the affected device.
        """

        rate: int
        """
        Number of operations per second.
        """

        @staticmethod
        def parse(iops_spec: dict[str, Value]) -> "BlockIOConfig.IOPS":
            """Parses a dictionary representing a IOPS configuration into a IOPS object.

            Args:
                iops_spec (dict[str, Value]): configuration values for this IOPS object.

            Returns:
                BlockIOConfig.IOPS: an object representing the IOPS specification
            """

            return BlockIOConfig.IOPS(
                path=iops_spec.get("path"), rate=int(iops_spec.get("rate"))
            )

    @dataclass
    class WeightDevice:
        """
        Define bandwidth for a given device.
        """

        path: str
        """
        Defines the symbolic path to the affected device.
        """

        weight: int
        """
        Integer value between 10 and 1000.
        """

        @staticmethod
        def parse(weight_device_spec: dict[str, Value]) -> "BlockIOConfig.WeightDevice":
            """Parses a dictionary representing a WeightDevice configuration into a WeightDevice object.

            Args:
                weight_device_spec (dict[str, Value]): configuration values for this WeightDevice object.

            Returns:
                BlockIOConfig.WeightDevice: an object representing the WeightDevice specification
            """

            return BlockIOConfig.WeightDevice(
                path=weight_device_spec.get("path"),
                weight=int(weight_device_spec.get("weight")),
            )

    device_read_bps: list[BPS]
    """
    BPS configuration for device reads.
    """
    device_write_bps: list[BPS]
    """
    BPS configuration for device writes.
    """

    device_read_iops: list[IOPS]
    """
    IOPS configuration for device read operations.
    """

    device_write_iops: list[IOPS]
    """
    IOPS configuration for device write operations.
    """

    weight_devices: list[WeightDevice]
    """
    Fine-tune bandwidth allocation by device
    """

    weight: int = field(default=500)
    """
    Modify the proportion of bandwidth allocated to a service relative to other services
    """

    @staticmethod
    def parse(block_io_config_spec: dict[str, Value]) -> "BlockIOConfig":

        return BlockIOConfig(
            device_read_bps=[
                BlockIOConfig.BPS.parse(bps_spec)
                for bps_spec in block_io_config_spec.get("device_read_bps", [])
            ],
            device_write_bps=[
                BlockIOConfig.BPS.parse(bps_spec)
                for bps_spec in block_io_config_spec.get("device_write_bps", [])
            ],
            device_read_iops=[
                BlockIOConfig.IOPS.parse(iops_spec)
                for iops_spec in block_io_config_spec.get("device_read_iops", [])
            ],
            device_write_iops=[
                BlockIOConfig.IOPS.parse(iops_spec)
                for iops_spec in block_io_config_spec.get("device_write_iops", [])
            ],
            weight_devices=[
                BlockIOConfig.WeightDevice.parse(weight_device_spec)
                for weight_device_spec in block_io_config_spec.get("weight_devices", [])
            ],
            weight=int(block_io_config_spec.get("weight", 500)),
        )


@dataclass
class ULimits:
    """
    Defines resource limits for a container
    """

    @dataclass
    class NumberOfFiles:
        """
        Soft and hard limits for a container.
        """

        soft: int
        """
        Soft limit for this container. Can be changed by non-root processes.
        """

        hard: int
        """
        Hard limit for this container. Cannot be changed by non-root processes.
        """

        @staticmethod
        def parse(number_of_files_spec: dict[str, Value]) -> "ULimits.NumberOfFiles":
            """Parses a dictionary representing a NumberOfFiles configuration into a NumberOfFiles object.

            Args:
                number_of_files_spec (dict[str, Value]): configuration values for this NumberOfFiles object.

            Returns:
                ULimits.NumberOfFiles: an object representing the NumberOfFiles specification
            """

            return ULimits.NumberOfFiles(
                soft=int(number_of_files_spec.get("soft")),
                hard=int(number_of_files_spec.get("hard")),
            )

    nofile: NumberOfFiles
    """
    Defines soft and hard limits for a container.
    """

    nproc: int
    """
    Defines the maximum number of processes that can be running.
    """

    @staticmethod
    def parse(ulimits_spec: dict[str, Value]) -> "ULimits":
        """Parses a dictionary representing a ULimits configuration into a ULimits object.

        Args:
            ulimits_spec (dict[str, Value]): configuration values for this ULimits object.

        Returns:
            ULimits: an object representing the ULimits specification
        """

        return ULimits(
            nofile=ULimits.NumberOfFiles.parse(
                number_of_files_spec=ulimits_spec.get("nofile", {})
            ),
            nproc=int(ulimits_spec.get("nproc", 65535)),
        )


@dataclass
class Secret:
    """
    Grants access to sensitive data defined by secrets on a per-service build basis.
    """

    source: str
    """
    The name of the secret as it exists on the platform.
    """

    target: Optional[str]
    """
    The name of the file to be mounted in /run/secrets/ in the service's task containers
    """

    uid: Optional[int | str]
    """
    The user ID (UID) to run the container process as.
    """

    gid: Optional[int | str]
    """
    The group ID (GID) to run the container process as.
    """

    mode: Optional[int] = field(default=0o444)
    """
    The permissions for the file to be mounted in the service's task containers, in octal notation.
    """

    @staticmethod
    def parse(secret_spec: dict[str, Value]) -> "Secret":
        """Parses a dictionary representing a Secret configuration into a Secret object.

        Args:
            secret_spec (dict[str, Value]): configuration values for this Secret object.

        Returns:
            Secret: an object representing the Secret specification
        """

        return Secret(
            source=secret_spec.get("source"),
            target=secret_spec.get("target"),
            uid=secret_spec.get("uid"),
            gid=secret_spec.get("gid"),
            mode=int(secret_spec.get("mode", 0o444)),
        )


@dataclass
class Config:
    """
    Configs allow services to adapt their behavior without the need to rebuild a Docker image
    """

    source: str
    """
    The name of the config as it exists on the platform.
    """

    target: Optional[str]
    """
    The name of the file to be mounted in the service's task containers.
    """

    uid: Optional[int | str]
    """
    The user ID (UID) to run the container process as.
    """

    gid: Optional[int | str]
    """
    The group ID (GID) to run the container process as.
    """

    mode: Optional[int] = field(default=0o444)
    """
    The permissions for the file to be mounted in the service's task containers, in octal notation.
    """

    @staticmethod
    def parse(config_spec: dict[str, Value]) -> "Config":
        """Parses a dictionary representing a Config configuration into a Config object.

        Args:
            config_spec (dict[str, Value]): configuration values for this Config object.

        Returns:
            Config: an object representing the Config specification
        """

        return Config(
            source=config_spec.get("source"),
            target=config_spec.get("target"),
            uid=config_spec.get("uid"),
            gid=config_spec.get("gid"),
            mode=int(config_spec.get("mode", 0o444)),
        )


@dataclass
class BuildSecretMap:
    """
    Grants access to sensitive data defined by secrets on a per-service build basis.
    """

    source: str
    """
    The name of the secret as it exists on the platform.
    """

    target: Optional[str]
    """
    The name of the file to be mounted in /run/secrets/ in the service's task containers
    """

    uid: Optional[int | str]
    """
    The user ID (UID) to run the container process as.
    """

    gid: Optional[int | str]
    """
    The group ID (GID) to run the container process as.
    """

    mode: Optional[int] = field(default=0o444)
    """
    The permissions for the file to be mounted in the service's task containers, in octal notation.
    """

    @staticmethod
    def parse(build_secret_map_spec: dict[str, Value]) -> "BuildSecretMap":
        """Parses a dictionary representing a BuildSecretMap configuration into a BuildSecretMap object.

        Args:
            build_secret_map_spec (dict[str, Value]): configuration values for this BuildSecretMap object.

        Returns:
            BuildSecretMap: an object representing the BuildSecretMap specification
        """

        return BuildSecretMap(
            source=build_secret_map_spec.get("source"),
            target=build_secret_map_spec.get("target"),
            uid=build_secret_map_spec.get("uid"),
            gid=build_secret_map_spec.get("gid"),
            mode=int(build_secret_map_spec.get("mode", 0o444)),
        )


@dataclass
class BuildSpecArgsList(list[Value]):
    """
    Representation of build arguments as a list.
    """


@dataclass
class BuildSpecArgsMap(dict[str, Value]):
    """
    Representation of build arguments as a mapping.
    """


@dataclass
class BuildSpec(HasLabels):
    """
    Specification of build configurations for a given service
    """

    context: str
    """
    The context from which to build an image for this service
    """

    dockerfile: Optional[str]
    """
    The name of the dockerfile to load when building an image for this service
    """

    dockerfile_inline: Optional[str]
    """
    Defines the Dockerfile content as an inlined string in a Compose file.
    """

    args: Optional[BuildSpecArgsList | BuildSpecArgsMap]
    """
    Arguments to pass to the build process when building an image for this service
    """

    ssh: Optional[list[Literal["default"] | str]]
    """
    Defines SSH authentications that the image builder should use during image build
    (e.g., cloning private repository).
    """

    cache_from: Optional[list[str]]
    """
    Defines a list of sources the image builder should use for cache resolution.
    """

    cache_to: Optional[list[str]]
    """
    Defines a list of export locations to be used to share build cache with future builds.
    """

    additional_contexts: Optional[list[str] | dict[str, str]]
    """
    Defines a list of named contexts the image builder should use during image build
    """

    extra_hosts: Optional[list[str] | dict[str, str]]
    """
    Adds extra hosts at build time.
    """

    isolation: Optional[str]
    """
    Specifies a build's container isolation technology. 
    
    This value is platform specific.
    """

    privileged: Optional[bool]
    """
    Configures the service image to build with elevated privileges.
    
    Support and actual impacts are platform specific.
    """

    no_cache: Optional[bool]
    """
    disables image builder cache and enforces a full rebuild from source
    for all image layers specified in the Dockerfile.
    """

    pull: Optional[bool]
    """
    Requires the image builder to pull referenced images (FROM Dockerfile directive),
    even if those are already available in the local image store.
    """

    network: Optional[str | Literal["none"]]
    """
    Set the network containers connect to for the RUN instructions during build.
    """

    shm_size: Optional[ByteValue | str]
    """
    Set the size of the /dev/shm partition for this build's containers.
    Specify as an int representing the number of bytes or as a string expressing a byte value.
    """

    target: Optional[str]
    """
    Build the specified stage as defined inside the Dockerfile.
    """

    secrets: Optional[str | BuildSecretMap]
    """
    Service build secrets
    """

    tags: Optional[list[str]]
    """
    Additional tags that must be associated with the built image.
    """

    ulimits: Optional[int | ULimits]
    """
    Configure ulimits for this container.
    """

    platforms: Optional[list[str]]
    """
    Defines a list of target platforms for built images.
    """

    @staticmethod
    def parse(build_spec_spec: dict[str, Value]) -> "BuildSpec":
        """Parses a dictionary representing a BuildSpec configuration into a BuildSpec object.

        Args:
            build_spec_spec (dict[str, Value]): configuration values for this BuildSpec object.

        Returns:
            BuildSpec: an object representing the BuildSpec specification
        """

        return BuildSpec(
            context=build_spec_spec.get("context"),
            dockerfile=build_spec_spec.get("dockerfile"),
            dockerfile_inline=build_spec_spec.get("dockerfile_inline"),
            args=build_spec_spec.get("args"),
            ssh=build_spec_spec.get("ssh"),
            cache_from=build_spec_spec.get("cache_from"),
            cache_to=build_spec_spec.get("cache_to"),
            additional_contexts=build_spec_spec.get("additional_contexts"),
            extra_hosts=build_spec_spec.get("extra_hosts"),
            isolation=build_spec_spec.get("isolation"),
            privileged=build_spec_spec.get("privileged"),
            no_cache=build_spec_spec.get("no_cache"),
            pull=build_spec_spec.get("pull"),
            network=build_spec_spec.get("network"),
            shm_size=build_spec_spec.get("shm_size"),
            target=build_spec_spec.get("target"),
            secrets=build_spec_spec.get("secrets"),
            tags=build_spec_spec.get("tags"),
            ulimits=build_spec_spec.get("ulimits"),
            platforms=build_spec_spec.get("platforms"),
        )


@dataclass(kw_only=True, slots=True, frozen=True)
class Service(HasLabels):
    """
    Representation of a docker-compose.yaml service mapping block.
    """

    annotations: Optional[list[str] | dict[str, str]] = None
    """
    Annotations for this service.
    """

    attach: Optional[bool] = None
    """
    When attach is defined and set to false Compose does not collect service logs,
    until you explicitly request it to.
    """

    build: str | BuildSpec
    """
    Build context configuration for this service.
    """

    blkio_config: Optional[BlockIOConfig] = None
    """
    Defines a set of configuration options to set block IO limits for a service
    """

    cpu_count: Optional[int] = None
    """
    Defines the number of usable CPUs for service container
    """

    cpu_percent: Optional[int] = None
    """
    Defines the usable percentage of the available CPUs.
    """

    cpu_shares: Optional[int] = None
    """
    Defines, as integer value, a service container's relative CPU weight versus other containers.
    """

    cpu_period: Optional[int] = None
    """
    Configures CPU CFS (Completely Fair Scheduler) period when a platform is based on Linux kernel.
    """

    cpu_quota: Optional[int] = None
    """
    Configures CPU CFS (Completely Fair Scheduler) quota when a platform is based on Linux kernel.
    """

    cpu_rt_runtime: Optional[Duration] = None
    """
    Configures CPU allocation parameters for platforms with support for realtime scheduler.
    
    It can be either an integer value using microseconds as unit or a duration.
    """

    cpu_rt_period: Optional[Duration] = None
    """
    Configures CPU allocation parameters for platforms with support for realtime scheduler.
    
    It can be either an integer value using microseconds as unit or a duration.
    """

    cpus: Optional[float] = None
    """
    Define the number of (potentially virtual) CPUs to allocate to service containers. 
    
    his is a fractional number. 0.000 means no limit.
    """

    cpuset: Optional[str] = None
    """
    Defines the explicit CPUs in which to allow execution. Can be a range 0-3 or a list 0,1
    """

    cap_add: Optional[list[str]] = None
    """
    Add container capabilities.
    """

    cap_drop: Optional[list[str]] = None
    """
    Drop container capabilities.
    """

    cgroup: Optional[str] = None
    """
    Specifies the cgroup namespace to join.
    
    When unset, it is the container runtime's decision to select which cgroup namespace to use,
    if supported.
    """

    cgroup_parent: Optional[str] = None
    """
    Optional parent cgroup for this container.
    """

    command: Optional[str | list[str] | Literal[""]] = None
    """
    Overrides the default command declared by the container image.
    """

    configs: Optional[list[str] | list[Config]] = None
    """
    Specifies configuration values accessible to this container.
    """

    container_name: Optional[str] = None
    """
    Overrides the default container computed by Compose.
    """

    credential_spec: Optional[
        CredentialSpecRegistry | CredentialSpecConfig | CredentialSpecFile
    ] = None
    """
    Credential specification for this managed services.
    """

    depends_on: Optional[list[str] | dict[str, DependencyConfig]] = None
    """
    Specifies services that this service depends on.
    """

    deploy: Optional[Deployment] = None
    """
    Specifies the configuration for the deployment and lifecycle of this service.
    """

    develop: Optional[Development] = None
    """
    Specifies the development configuration for maintaining a container in sync with source.
    """

    device_cgroup_rules: Optional[list[str]] = None
    """
    Defines a list of device cgroup rules for this container.
    """

    devices: Optional[list[str]] = None
    """
    Defines a list of device mappings for created containers.
    """

    dns: Optional[str | list[str]] = None
    """
    Defines custom DNS servers to set on the container network interface configuration.
    """

    dns_opt: Optional[list[str]] = None
    """
    List custom DNS options to be passed to the container’s DNS resolver.
    """

    dns_search: Optional[list[str]] = None
    """
    Defines custom DNS search domains to set on container network interface configuration.
    """

    domainname: Optional[str] = None
    """
    Declares a custom domain name to use for the service container.
    """

    entrypoint: Optional[str | list[str] | Literal[None, ""]] = None
    """
    Declares the default entrypoint for the service container.
    """

    env_file: Optional[str | list[str] | list[EnvFile]] = None
    """
    Adds environment variables to the container based on the file content.
    """

    environment: Optional[list[Value] | dict[str, Value]] = None
    """
    Environment values set in the container.
    """

    expose: Optional[list[str]] = None
    """
    Defines the (incoming) port or a range of ports that Compose exposes from the container.
    """

    extends: Optional[list[ExtensionsSpec]] = None
    """
    Defines extensions to this compose service.
    """

    external_links: Optional[list[str]] = None
    """
    Links service containers to services managed outside of your Compose application.
    """

    extra_hosts: Optional[list[str] | dict[str, str]] = None
    """
    Adds hostname mappings to the container network interface configuration.
    """

    group_add: Optional[list[str | int]] = None
    """
    Specifies additional groups, by name or number,
    which the user inside the container must be a member of.
    """

    healthcheck: Optional[HealthCheck] = None
    """
    Defines the configuration used to verify the health of this service's container.
    """

    hostname: Optional[str] = None
    """
    Defines a custom hostname for the container.
    """

    image: Optional[str] = None
    """
    Specifies the image to start the container from.
    """

    init: Optional[bool] = None
    """
    Runs an init process (PID 1) inside the container that forwards signals and reaps processes.
    Set this option to true to enable this feature for the service.
    """

    ipc: Optional[Literal["shareable"] | IPCService] = None
    """
    Configures the IPC isolation mode set by the service container.
    """

    isolation: Optional[str] = None
    """
    Specifies a build's container isolation technology. 
    
    This value is platform specific.
    """

    links: Optional[list[str]] = None
    """
    Defines a network link to containers in another service.
    """

    logging: Optional[LoggingConfig] = None
    """
    Configures the logging subsystem for this service container.
    """

    mac_address: Optional[str] = None
    """
    Sets a mac_address for the service container.
    """

    mem_limit: Optional[ByteValue] = None
    """
    Configures a limit on the amount of memory a container can allocate.
    """

    mem_reservation: Optional[ByteValue] = None
    """
    Configures a reservation on the amount of memory a container can allocate.
    """

    mem_swappiness: Optional[int] = None
    """
    Defines as a percentage, a value between 0 and 100,
    for the host kernel to swap out anonymous memory pages used by a container
    """

    memswap_limit: Optional[ByteValue] = None
    """
    Controls the amount of memory a container can swap to disk.
    """

    network_mode: Optional[Literal["none", "host"] | NetworkMode] = None
    """
    Sets a service container's network mode.
    """

    networks: Optional[list[str] | dict[str, NetworkSpec]] = None
    """
    Configures networks to which this service's container should connect to.
    """

    oom_kill_disable: Optional[bool] = None
    """
    Disables OOM Killer for this container.
    """

    oom_score_adj: Optional[int] = None
    """
    Tunes the preference for containers to be killed by platform in case of memory starvation
    """

    pid: Optional[int] = None
    """
    Sets the PID mode for container created by Compose
    """

    pids_limit: Optional[Literal[-1] | int] = None
    """
    Tunes a container’s PIDs limit
    """

    platform: Optional[str] = None
    """
    Defines the target platform the containers for the service run on.
    """

    ports: Optional[list[str] | list[PortSpec]] = None
    """
    Exposes container ports.
    """

    privileged: Optional[bool] = None
    """
    Configures the service container to run with elevated privileges
    """

    profiles: Optional[list[str]] = None
    """
    Defines a list of named profiles for the service to be enabled under
    """

    pull_policy: Optional[
        Literal["always", "never", "missing", "build", "if_not_present"]
    ] = field(default="missing")
    """
    Defines the decisions Compose makes when it starts to pull images
    """

    read_only: Optional[bool] = None
    """
    Configures the service container to be read-only.
    """

    restart: Optional[
        Literal["no", "always", "unless-stopped"] | FailureRestartPolicy
    ] = field(default="no")
    """
    Defines the policy that the platform applies on container termination.
    """

    runtime: Optional[Literal["runc"]] = field(default="runc")
    """
    Specifies which runtime to use for the service’s containers.
    """

    scale: Optional[int] = None
    """
    Specifies the default number of containers to deploy for this service
    """

    secrets: Optional[list[str] | dict[str, Secret]] = None
    """
    Grants access to sensitive data defined by secrets on a per-service basis.
    """

    security_opt: Optional[list[str]] = None
    """
    Overrides the default labeling scheme for each container.
    """

    shm_size: Optional[ByteValue] = None
    """
    Configures the size of the shared memory
    """

    stdin_open: Optional[bool] = None
    """
    Configures a service containers to run with an allocated stdin.
    """

    stop_grace_period: Optional[Duration] = None
    """
    Duration of time for a container to stop gracefully before the Docker Engine forcefully kills it.
    """

    stop_signal: Optional[str] = None
    """
    Defines the signal that Compose uses to stop the service containers
    """

    storage_opt: dict[str, Value] = None
    """
    Defines storage driver options for a service.
    """

    sysctl: Optional[list[str] | dict[str, Value]] = None
    """
    Defines kernel parameters to set in the container.
    """

    tmpfs: Optional[str | list[str]] = None
    """
    Mounts a temporary file system inside the container.
    """

    tty: Optional[bool] = None
    """
    Configures a service container to run with a TTY.
    """

    ulimits: Optional[int | ULimits] = None
    """
    Overrides the default ulimits for a container.
    """

    user: Optional[str] = None
    """
    Overrides the user used to run the container process.
    """

    userns_mode: Optional[str] = None
    """
    Sets the user namespace for the service.
    """

    uts: Optional[Literal["host"]] = None
    """
    Configures the UTS namespace mode set for the service container.-
    """

    volumes: Optional[list[Volume]] = None
    """
    Define mount host paths or named volumes that are accessible by service containers
    """

    volumes_from: Optional[list[str]] = None
    """
    Attach volumes from other services.
    """

    working_dir: Optional[str] = None
    """
    Overrides the container 's working directory which is specified by the image.
    """

    @staticmethod
    def parse(service_spec: dict[str, Value]):
        """
        Parses a service specification and returns a Service object.

        :param service_name: The name of the service.
        :type service_name: str
        :param service_spec: The service specification.
        :type service_spec: dict[str, Value]
        :return: A Service object.
        :rtype: Service
        """

        working_dir = service_spec.get("working_dir", None)
        image = service_spec.get("image", None)
        command = service_spec.get("command", None)
        entrypoint = service_spec.get("entrypoint", None)
        env_file = service_spec.get("env_file", None)
        environment = service_spec.get("environment", None)
        expose = service_spec.get("expose", None)
        links = service_spec.get("links", None)
        volumes = service_spec.get("volumes", None)
        volumes_from = service_spec.get("volumes_from", None)
        depends_on = service_spec.get("depends_on", None)
        networks = service_spec.get("networks", None)
        secrets = service_spec.get("secrets", None)
        build = service_spec.get("build", None)
        logging = service_spec.get("logging", None)
        healthcheck = service_spec.get("healthcheck", None)
        depends_on = service_spec.get("depends_on", None)
        deploy = service_spec.get("deploy", None)
        mode = service_spec.get("mode", None)
        restart = service_spec.get("restart", None)
        stop_grace_period = service_spec.get("stop_grace_period", None)
        stop_signal = service_spec.get("stop_signal", None)
        sysctls = service_spec.get("sysctls", None)
        tmpfs = service_spec.get("tmpfs", None)
        cap_add = service_spec.get("cap_add", None)
        cap_drop = service_spec.get("cap_drop", None)

        service = Service(
            image=image,
            command=command,
            entrypoint=entrypoint,
            env_file=env_file,
            environment=environment,
            expose=expose,
            links=links,
            volumes=volumes,
            volumes_from=volumes_from,
            depends_on=depends_on,
            networks=networks,
            secrets=secrets,
            build=build,
            logging=logging,
            healthcheck=healthcheck,
            deploy=deploy,
            restart=restart,
            stop_grace_period=stop_grace_period,
            stop_signal=stop_signal,
            tmpfs=tmpfs,
            cap_add=cap_add,
            cap_drop=cap_drop,
            working_dir=working_dir,
            mac_address=service_spec.get("mac_address", None),
            mem_limit=service_spec.get("mem_limit", None),
            mem_reservation=service_spec.get("mem_reservation", None),
            mem_swappiness=service_spec.get("mem_swappiness", None),
            memswap_limit=service_spec.get("memswap_limit", None),
            network_mode=service_spec.get("network_mode", None),
            oom_kill_disable=service_spec.get("oom_kill_disable", None),
            oom_score_adj=service_spec.get("oom_score_adj", None),
            pid=service_spec.get("pid", None),
            pids_limit=service_spec.get("pids_limit", None),
            platform=service_spec.get("platform", None),
            ports=service_spec.get("ports", None),
            privileged=service_spec.get("privileged", None),
            profiles=service_spec.get("profiles", None),
            pull_policy=service_spec.get("pull_policy", None),
            read_only=service_spec.get("read_only", None),
            runtime=service_spec.get("runtime", None),
            scale=service_spec.get("scale", None),
            security_opt=service_spec.get("security_opt", None),
            shm_size=service_spec.get("shm_size", None),
            stdin_open=service_spec.get("stdin_open", None),
            storage_opt=service_spec.get("storage_opt", None),
            sysctl=sysctls,
            tty=service_spec.get("tty", None),
            ulimits=service_spec.get("ulimits", None),
            user=service_spec.get("user", None),
            userns_mode=service_spec.get("userns_mode", None),
            uts=service_spec.get("uts", None),
        )
        # service.labels = service_spec.get("labels", None)

        return service
