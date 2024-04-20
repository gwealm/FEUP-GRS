"""
Model representations of various docker-compose.yaml block mappings.
"""

from .volume import Volume, DriverOptions as VolumeDriverOptions
from .network import Network, IPAM, IPAMConfig, DriverOptions as NetworkDriverOptions
from .service import Service
from .config import Config, DriverOptions as ConfigDriverOptions
from .secret import Secret
