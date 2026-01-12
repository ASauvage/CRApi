from dataclasses import dataclass


@dataclass
class Arena:
    id: int
    name: str
    raw_name: str

    @classmethod
    def from_api(cls, data: dict) -> "Arena":
        return cls(
            id=data["id"],
            name=data["name"],
            raw_name=data["rawName"]
        )
