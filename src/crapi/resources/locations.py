from ..http.client import HttpClient
from ..models import Location


class LocationsRessource:
    """
    Access global and local rankings
    """
    def __init__(self, client: HttpClient) -> None:
        self.client = client
    
    def list_locations(self, **kwargs) -> list[Location]:
        """List all locations

        :return: list of locations
        """
        data = self.client.get("/locations", params=kwargs)
        return [Location.from_api(location) for location in data]
