from dataclasses import dataclass
from typing import Literal
from datetime import datetime

from . import ClanWarParticipant, ClanWarClan


@dataclass
class ClanCurrentWar:
    state: Literal["CLAN_NOT_FOUND", "ACCESS_DENIED", "NOT_IN_WAR", "COLLECTION_DAY", "MATCHMAKING", "WAR_DAY", "ENDED"]
    clan: ClanWarClan
    participants: list[ClanWarParticipant]
    clans: list[ClanWarClan]
    collection_end_time: datetime
    war_end_time: datetime

    @classmethod
    def from_api(cls, data: dict) -> "ClanCurrentWar":
        return cls(
            state=data["state"],
            clan=ClanWarClan.from_api(data["clan"]),
            participants=[ClanWarParticipant.from_api(participant) for participant in data["participants"]],
            clans=[ClanWarClan.from_api(clan) for clan in data["clans"]],
            collection_end_time=datetime.fromisoformat(data["collectionEndTime"]),
            war_end_time=datetime.fromisoformat(data["warEndTime"])
        )
