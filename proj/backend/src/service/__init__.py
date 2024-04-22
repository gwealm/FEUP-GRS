"""
Services that are deployable to any new network segment.
"""

from abc import ABC

from engine.models.host import Host


class Service(ABC):
    """Service is a generic service that can be deployed to any network"""

    def __init__(self, name: str, host: Host):
        """Constructs a Service object, which can be deployed to any new network segment.

        Args:
            name (str): the name of this service
            host (Host): the host where this service will run.
        """
        self.name = name
        self.host = host
