from dataclasses import dataclass
from datetime import datetime

from . import ClanWarParticipant, ClanWarStanding


@dataclass
class ClanWarLog:
    season_id: int
    participants: list[ClanWarParticipant]
    standings: list[ClanWarStanding]
    date: datetime

    @classmethod
    def from_api(cls, data: dict) -> "ClanWarLog":
        return cls(
            season_id=data["seasonId"],
            participants=[ClanWarParticipant.from_api(participant) for participant in data["participants"]],
            standings=[ClanWarStanding.from_api(standing) for standing in data["standings"]],
            date=datetime.fromisoformat(data["date"]),
        )
