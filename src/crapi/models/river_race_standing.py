from dataclasses import dataclass

from . import RiverRaceClan


@dataclass
class RiverRaceStanding:
    rank: int
    trophy_change: int
    clan: RiverRaceClan

    @classmethod
    def from_api(cls, data: dict) -> "RiverRaceStanding":
        return cls(
            rank=int(data["rank"]),
            trophy_change=int(data["trophyChange"]),
            clan=RiverRaceClan.from_api(data["clan"])
        )
