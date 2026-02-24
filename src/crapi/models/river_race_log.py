from dataclasses import dataclass
from datetime import datetime

from . import RiverRaceStanding


@dataclass
class RiverRaceLog:
    season_id: int
    section_index: int
    standings: list[RiverRaceStanding]
    created_date: datetime

    @classmethod
    def from_api(cls, data: dict) -> "RiverRaceLog":
        return cls(
            season_id=int(data["seasonId"]),
            section_index=int(data["sectionIndex"]),
            standings=[RiverRaceStanding.from_api(standing) for standing in data["standings"]],
            created_date=datetime.fromisoformat(data["createdDate"])
        )
