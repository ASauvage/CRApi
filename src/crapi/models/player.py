from dataclasses import dataclass


@dataclass
class Player:
    tag: str
    name: str
    trophies: int
    exp_level: int

    @classmethod
    def from_api(cls, data: dict) -> "Player":
        return cls(
            tag=data["tag"],
            name=data["name"],
            trophies=data["trophies"],
            exp_level=data["expLevel"]
        )
