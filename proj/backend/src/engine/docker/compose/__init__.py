"""_summary_
"""

import subprocess
import shlex
import tempfile
from typing import Optional

from .manifest import Manifest
from .handler import DockerComposeManifestHandler


# FIXME: advanced development would do this through the docker IPC socket.
class DockerCompose:
    """_summary_"""

    def __init__(self, manifest_handler: Optional[DockerComposeManifestHandler] = None):
        self.handler = (
            manifest_handler
            if manifest_handler is not None
            else DockerComposeManifestHandler()
        )

    def provision(self, manifest: Manifest):
        """Provisions the project representation by the given Manifest

        Args:
            manifest (Manifest): a Manifest object representing a Compose project
        """

        manifest_str = self.handler.dump(manifest)
        with tempfile.NamedTemporaryFile(mode="+w", encoding="utf-8") as tmp_file:

            with tmp_file.file as f:
                f.write(manifest_str)

            try:
                subprocess.run(
                    shlex.split(f"docker compose -f {tmp_file.name} up -d"),
                    check=True,
                    capture_output=True,
                )
            except subprocess.CalledProcessError:
                pass

    def tear_down(self, manifest: Manifest):
        """Tears down the Compose project represented by the given Manifest

        Args:
            manifest (Manifest): a Manifest object representing a Compose project
        """

        manifest_str = self.handler.dump(manifest)
        with tempfile.NamedTemporaryFile(mode="+w", encoding="utf-8") as tmp_file:

            with tmp_file.file as f:
                f.write(manifest_str)

            try:
                subprocess.run(
                    shlex.split(f"docker compose -f {tmp_file.name} down"),
                    check=True,
                    capture_output=True,
                )
            except subprocess.CalledProcessError:
                pass

    def is_available(self) -> bool:
        """Returns whether Docker compose is available on this system.

        Returns:
            bool: Whether Docker Compose is available on this system or not
        """

        try:
            subprocess.run(
                shlex.split("docker compose version"), check=True, capture_output=True
            )
            return True
        except subprocess.CalledProcessError:
            return False
