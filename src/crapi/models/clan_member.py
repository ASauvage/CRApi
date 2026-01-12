from dataclasses import dataclass
from typing import Literal
from datetime import datetime

from . import Arena


@dataclass
class ClanMember:
    tag: str
    name: str
    role: Literal["leader", "coLeader", "elder", "member"]
    last_seen: datetime
    exp_level: int
    trophies: int
    arena: Arena
    clan_rank: int
    previous_clan_rank: int
    donations: int
    donations_received: int
    clan_chest_points: int

    @classmethod
    def from_api(cls, data: dict) -> "ClanMember":
        return cls(
            tag=data["tag"],
            name=data["name"],
            role=data["role"],
            last_seen=datetime.fromisoformat(data["lastSeen"]),
            exp_level=data["expLevel"],
            trophies=data["trophies"],
            arena=Arena.from_api(data["arena"]),
            clan_rank=data["clanRank"],
            previous_clan_rank=data["previousClanRank"],
            donations=data["donations"],
            donations_received=data["donationsReceived"],
            clan_chest_points=data["clanChestPoints"]
        )
