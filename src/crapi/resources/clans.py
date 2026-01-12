from ..http.client import HttpClient
from ..models import Clan


class ClansResource:
    """Access clan specific information.
    """
    def __init__(self, client: HttpClient) -> None:
        self.client = client
    
    def get_by_tag(self, tag: str) -> Clan:
        """Get information about a single clan by clan tag.

        :param tag: Tag of the clan.
        :return: Clan
        """
        data = self.client.get(f"/clans/{tag}")
        return Clan.from_api(data)
