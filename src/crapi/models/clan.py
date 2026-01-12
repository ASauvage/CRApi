from dataclasses import dataclass
from typing import Literal

from . import Location, ClanMember


@dataclass
class Clan:
    tag: str
    name: str
    description: str
    badge_id: str
    location: Location
    open_type: Literal["OPEN", "INVITE_ONLY", "CLOSED"]
    required_trophies: int
    members_trophies: int
    war_trophies: int
    donations_per_week: int
    members_count: int
    members: list[ClanMember]
    
    @classmethod
    def from_api(cls, data: dict) -> "Clan":
        return cls(
            tag=data["tag"],
            name=data["name"],
            description=data["description"],
            badge_id=data["badgeId"],
            location=Location.from_api(data["location"]),
            open_type=data["type"],
            required_trophies=data["requiredTrophies"],
            members_trophies=data["clanScore"],
            war_trophies=data["clanWarTrophies"],
            donations_per_week=data["donationsPerWeek"],
            members_count=data["members"],
            members=[ClanMember.from_api(player) for player in data["memberList"]]
        )
