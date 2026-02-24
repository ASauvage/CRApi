from dataclasses import dataclass
from datetime import datetime

from . import RiverRaceParticipant


@dataclass
class RiverRaceClan:
    tag: str
    clan_score: int
    badge_id: int
    name: str
    fame: int
    repair_points: int
    finish_time: datetime
    participants: list[RiverRaceParticipant]
    period_points: int

    @classmethod
    def from_api(cls, data: dict) -> "RiverRaceClan":
        return cls(
            tag=data["tag"],
            clan_score=int(data["clanScore"]),
            badge_id=int(data["badgeId"]),
            name=data["name"],
            fame=int(data["fame"]),
            repair_points=int(data["repairPoints"]),
            finish_time=datetime.fromisoformat(data["finishTime"]),
            participants=[RiverRaceParticipant.from_api(participant) for participant in data["participants"]],
            period_points=int(data["periodPoints"])
        )
