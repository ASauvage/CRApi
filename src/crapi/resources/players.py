from ..http.client import HttpClient
from ..commons.utils import build_path
from ..models import Player


class PlayersResource:
    """Access player specific information.
    """
    def __init__(self, client: HttpClient) -> None:
        self.client = client
    
    def get_by_tag(self, tag: str) -> Player:
        """Get information about a single player by player tag.

        :param tag: Tag of the player.
        :return: Player Object
        """
        data = self.client.get(build_path("players", tag))
        return Player.from_api(data)
