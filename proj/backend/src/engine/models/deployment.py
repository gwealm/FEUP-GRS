"""
"""

from .network import Network


class Deployment:
    """ """

    def __init__(self, team_name: str, team_network: Network):
        self.team_name = team_name
        self.team_network = team_network
