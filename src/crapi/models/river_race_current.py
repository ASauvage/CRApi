from dataclasses import dataclass
from datetime import datetime
from typing import Literal

from . import RiverRaceClan, PeriodLog


@dataclass
class CurrentRiverRace:
    state: Literal["CLAN_NOT_FOUND", "ACCESS_DENIED", "MATCHMAKING", "MATCHED", "FULL", "ENDED"]
    clan: RiverRaceClan
    clans: list[RiverRaceClan]
    collection_end_time: datetime
    war_end_time: datetime
    section_index: int
    period_index: int
    period_type: Literal["TRAINING", "WAR_DAY", "COLOSSEUM"]
    period_logs: list[PeriodLog]

    @classmethod
    def from_api(cls, data: dict) -> "CurrentRiverRace":
        return cls(
            state=data["state"],
            clan=RiverRaceClan.from_api(data["clan"]),
            clans=[RiverRaceClan.from_api(riverraceclan) for riverraceclan in data["clans"]],
            collection_end_time=datetime.fromisoformat(data["collectionEndTime"]),
            war_end_time=datetime.fromisoformat(data["warEndTime"]),
            section_index=int(data["sectionIndex"]),
            period_index=int(data["periodIndex"]),
            period_type=data["periodType"],
            period_logs=[PeriodLog.from_api(periodlog) for periodlog in data["periodLogs"]]
        )
