from .http.client import HttpClient
from .resources import ClansResource, LocationsResource, PlayersResource


class CRApiClient:
    def __init__(self, token: str | None = None, version: str = "v1") -> None:
        http = HttpClient(
            hostname="https://api.clashroyale.com/",
            version=version,
            token=token
        )

        # self.cards = CardsResource(http)
        # self.challenges = ChalengesResource(http)
        self.clans = ClansResource(http)
        self.locations = LocationsResource(http)
        self.players = PlayersResource(http)
        # self.tournaments = TournamentsResource(http)
