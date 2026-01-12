from .http.client import HttpClient
from .resources import ClansResource, PlayersRessource


class CRApiClient:
    def __init__(self, token: str | None = None, version: str = "v1") -> None:
        http = HttpClient(
            hostname="https://api.clashroyale.com/",
            version=version,
            token=token
        )

        self.clans = ClansResource(http)
        self.players = PlayersRessource(http)
