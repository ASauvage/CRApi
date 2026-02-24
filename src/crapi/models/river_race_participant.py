from dataclasses import dataclass


@dataclass
class RiverRaceParticipant:
    tag: str
    name: str
    fame: int
    repair_points: int
    boat_attacks: int
    decks_used: int
    decks_used_today: int

    @classmethod
    def from_api(cls, data: dict) -> "RiverRaceParticipant":
        return cls(
            tag=data["tag"],
            name=data["name"],
            fame=int(data["fame"]),
            repair_points=int(data["repairPoints"]),
            boat_attacks=int(data["boatAttacks"]),
            decks_used=int(data["decksUsed"]),
            decks_used_today=int(data["decksUsedToday"])
        )
