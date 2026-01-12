from .http.client import HttpClient
from .resources import ClansRessources, PlayersRessource


class CRApiClient:
    def __init__(self, token: str | None = None, version: str = "v1") -> None:
        http = HttpClient(
            base_url="",
            token=token
        )

        self.clans = ClansRessources(http)
        self.players = PlayersRessource(http)
