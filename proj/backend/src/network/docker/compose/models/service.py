"""
Classes related to service configuration specifications inside a docker-compose.yaml file.
"""

from typing import Optional, Literal
from dataclasses import dataclass, field

from .traits import HasLabels
from .types import Duration, ByteValue, Value


@dataclass
class Volume:
    """
    Volume mounted on a container through a filesystem bind.
    """

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


@dataclass
class FailureRestartPolicy:
    """
    Policy applied when restarting a service container.
    """

    max_retries: Optional[int] = None
    """
    Max number of retries for terminated containers.
    """


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


@dataclass
class Development:
    """
    Specifications of how to maintain a service in sync with source.
    """

    watch: list[DevelopmentWatch]
    """
    Defines a list of rules that control automatic service updates based on local file changes.
    """


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


@dataclass
class CredentialSpecFile:
    """
    Specifies a CredentialSpec inside a file
    """

    file: str
    """
    The path of the file containing the CredentialSpec
    """


@dataclass
class CredentialSpecRegistry:
    """
    Specifies a CredentialSpec inside a registry
    """

    registry: str
    """
    The path of the registry containing the CredentialSpec
    """


@dataclass
class CredentialSpecConfig:
    """
    Specifies a CredentialSpec inside a config
    """

    config: str
    """
    The path of the config containing the CredentialSpec
    """


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

    nofile: NumberOfFiles
    """
    Defines soft and hard limits for a container.
    """

    nproc: int
    """
    Defines the maximum number of processes that can be running.
    """


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
