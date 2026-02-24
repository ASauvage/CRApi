from dataclasses import dataclass

from . import ClanWarClan


@dataclass
class ClanWarStanding:
    trophy_change: int
    clan: ClanWarClan

    @classmethod
    def from_api(cls, data: dict) -> "ClanWarStanding":
        return cls(
            trophy_change=int(data["trophyChange"]),
            clan=ClanWarClan.from_api(data["clan"])
        )
