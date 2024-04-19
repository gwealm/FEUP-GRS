from dataclasses import dataclass, field

import yaml
from yaml import Loader

from typing import Optional

from .models import Config, Service, Secret, Network, Volume
from .models.types import Value


@dataclass
class DockerComposeManifest:
    """
    Representation of a docker-compose.yaml manifest file.
    """

    version: float = 3.8
    services: dict[str, Service] | list[str] = field(default_factory=dict)
    networks: dict[str, Network] | list[str] = field(default_factory=dict)
    volumes: dict[str, Volume] | list[str] = field(default_factory=dict)
    secrets: dict[str, Secret] | list[str] = field(default_factory=dict)
    configs: dict[str, Config] | list[str] = field(default_factory=dict)


class DockerComposeManifestTemplate:
    """
    Representation of a docker-compose.yaml manifest file template.

    This file is populated with given values to generate a concrete manifest.
    """

    def __init__(self, manifest_str: str):
        self.manifest_str = manifest_str

    def compile(
        self, values: Optional[dict[str, Value]] = None
    ) -> DockerComposeManifest:
        """_summary_

        Args:
            values (dict): _description_

        Returns:
            DockerComposeManifest: _description_
        """
        if values is None:
            values = {}

        for key, value in values.items():
            pattern = f"{{{{ {key} }}}}"

            self.manifest_str = self.manifest_str.replace(pattern, str(value))

        yaml_object = yaml.safe_load(self.manifest_str)

        return self._parse_yaml_manifest_object(yaml_object)

    def _parse_yaml_manifest_object(
        self, yaml_object: dict[str, Value]
    ) -> DockerComposeManifest:

        services = []
        if "services" in yaml_object:
            service_specs = yaml_object.get("services")

            for service_name in service_specs:
                service_spec = service_specs.get(service_name, None)

                if service_spec is not None:
                    services.append(Service.parse(service_spec))
                else:
                    services.append(service_name)

        volumes = []
        if "volumes" in yaml_object:
            volume_specs = yaml_object.get("volumes")

            for volume_name in volume_specs:
                volume_spec = volume_specs.get(volume_name, None)

                if volume_spec is not None:
                    volumes.append(Volume.parse(volume_name, volume_spec))
                else:
                    volumes.append(volume_name)

        configs = []
        if "configs" in yaml_object:
            config_specs = yaml_object.get("configs")

            for config_name in config_specs:
                config_spec = config_specs.get(config_name, None)

                if config_spec is not None:
                    configs.append(Config.parse(config_name, config_spec))
                else:
                    configs.append(config_name)

        secrets = []
        if "secrets" in yaml_object:
            secret_specs = yaml_object.get("secrets")

            for secret_name in secret_specs:
                secret_spec = secret_specs.get(secret_name, None)

                if secret_spec is not None:
                    secrets.append(Secret.parse(secret_name, secret_spec))
                else:
                    secrets.append(secret_name)

        networks = []
        if "networks" in yaml_object:
            network_specs = yaml_object.get("networks")

            for network_name in network_specs:
                network_spec = network_specs.get(network_name, None)

                if network_spec is not None:
                    networks.append(Network.parse(network_name, network_spec))
                else:
                    networks.append(network_name)

        return DockerComposeManifest(
            services=services,
            networks=networks,
            volumes=volumes,
            configs=configs,
            secrets=secrets,
        )
