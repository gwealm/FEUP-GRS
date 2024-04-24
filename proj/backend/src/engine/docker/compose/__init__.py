"""_summary_
"""

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
        """_summary_

        Returns:
            bool: _description_
        """
        return True