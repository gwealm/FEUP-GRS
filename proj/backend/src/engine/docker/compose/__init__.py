"""_summary_
"""

import subprocess
import shlex

from .manifest import Manifest


class DockerCompose:
    """_summary_"""

    def __init__(self):
        pass

    def provision(self, manifest: Manifest):
        """_summary_

        Args:
            manifest (DockerComposeManifest): _description_
        """

    def tear_down(self, manifest: Manifest):
        """_summary_

        Args:
            manifest (DockerComposeManifest): _description_
        """

    def is_available(self) -> bool:
        """Returns whether Docker compose is available on this system.

        Returns:
            bool: Whether Docker Compose is available on this system or not
        """

        try:
            subprocess.run(shlex.split("docker compose version"), check=True)
            return True
        except subprocess.CalledProcessError:
            return False
