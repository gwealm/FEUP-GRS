"""_summary_
"""

import yaml

from .manifest import ManifestTemplate, Manifest
from .models.traits import GenerateConfig


class DockerComposeManifestHandler:
    """
    Loads a docker-compose.yaml manifest file.
    """

    def __init__(self):
        pass

    def load(self, path: str) -> ManifestTemplate:
        """Loads a docker-compose.yaml manifest file and

        returns a DockerComposeManifestTemplate object.

        Args:
            path (str): the path to the docker-compose.yaml manifest file

        Returns:
            ManifestTemplate: An object which can generate a concrete manifest.
        """

        with open(path, "r", encoding="utf-8") as f:
            manifest_str = f.read()

            manifest = ManifestTemplate(manifest_str)

            return manifest

    def dump(self, manifest: Manifest):
        """
        Dumps the given manifest to a YAML-formatted string.

        Args:
            manifest (Manifest): the manifest to dump
        """

        config = {}

        services = {}
        for service_name, service in manifest.services.items():
            services[service_name] = service.to_dict()
        config["services"] = services

        if len(manifest.configs) > 0:
            configs = {}

            for config_name, config in manifest.configs.items():
                value = (
                    config.to_dict() if isinstance(config, GenerateConfig) else config
                )

                configs[config_name] = value if value != config_name else {}

            config["configs"] = configs

        if len(manifest.secrets) > 0:
            secrets = {}

            for secret_name, secret in manifest.secrets.items():
                value = (
                    secret.to_dict() if isinstance(secret, GenerateConfig) else secret
                )

                secrets[secret_name] = value if value != secret_name else {}

            config["secrets"] = secrets

        if len(manifest.networks) > 0:
            networks = {}

            for network_name, network in manifest.networks.items():
                value = (
                    network.to_dict()
                    if isinstance(network, GenerateConfig)
                    else network
                )

                networks[network_name] = value if value != network_name else {}

            config["networks"] = networks

        if len(manifest.volumes) > 0:
            volumes = {}

            for volume_name, volume in manifest.volumes.items():
                value = (
                    volume.to_dict() if isinstance(volume, GenerateConfig) else volume
                )

                volumes[volume_name] = value if value != volume_name else {}

            config["volumes"] = volumes

        return yaml.dump(config)
