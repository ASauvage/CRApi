from dataclasses import dataclass

from . import ClanWarParticipant


@dataclass
class ClanWarClan:
    tag: str
    name: str
    members_trophies: int
    crowns: int
    badge_id: int
    participants: list[ClanWarParticipant]
    battles_played: int
    wins: int

    @classmethod
    def from_api(cls, data: dict) -> "ClanWarClan":
        return cls(
            tag=data["tag"],
            name=data["name"],
            members_trophies=data["clanScore"],
            crowns=data["crowns"],
            badge_id=data["badgeId"],
            participants=[ClanWarParticipant.from_api(participant) for participant in data["participants"]],
            battles_played=data["battles_played"],
            wins=data["wins"]
        ) 
