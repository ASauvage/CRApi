from ..http.client import HttpClient
from ..commons.utils import build_path, params_format
from ..models import Clan, ClanMember


class ClansResource:
    """Access clan specific information.
    """
    def __init__(self, client: HttpClient) -> None:
        self.client = client
    
    def search(self, name: str | None = None, location_id: int | None = None, min_members: int | None = None, max_members: int | None = None,
               min_members_trophies: int | None = None, limit: int | None = None, after: str | None = None, before: str | None = None) -> list[Clan]:
        """Search all clans by name and/or filtering the results using various criteria.

        :param name: Search clans by name.
        :param location_id: Filter by clan location identifier.
        :param min_members: Filter by minimum number of clan members.
        :param max_members: Filter by maximum number of clan members.
        :param min_members_trophies: Filter by minimum amount of clan score.
        :param limit: Limit the number of items returned in the response.
        :param after: Return only items that occur after this marker.
        :param before: Return only items that occur before this marker.
        :return: List of Clan Object
        """
        data = self.client.get(build_path("clans"), params=params_format(
            name=name,
            locationId=location_id,
            minMembers=min_members,
            maxMembers=max_members,
            minScore=min_members_trophies,
            limit=limit,
            after=after,
            before=before
        ))
        return [Clan.from_api(clan) for clan in data]
    
    def get_by_tag(self, tag: str) -> Clan:
        """Get information about a single clan by clan tag.

        :param tag: Tag of the clan.
        :return: Clan Object
        """
        data = self.client.get(build_path("clans", tag))
        return Clan.from_api(data)

    def get_war_log(self, tag: str) -> None:
        pass

    def get_current_war(self, tag: str) -> None:
        pass

    def get_river_race_log(self, tag: str) -> None:
        pass

    def get_current_river_race(self, tag: str) -> None:
        pass

    def get_members(self, tag: str, limit: int | None = None, after: str | None = None, before: str | None = None) -> list[ClanMember]:
        """List clan members.

        :param tag: Tag of the clan.
        :param limit: Limit the number of items returned in the response.
        :param after: Return only items that occur after this marker.
        :param before: Return only items that occur before this marker.
        :return: List of ClanMember Object
        """
        data = self.client.get(build_path("clans", tag, "members"), params=params_format(
            limit=limit,
            after=after,
            before=before
        ))
        return [ClanMember.from_api(member) for member in data]
