from dataclasses import dataclass


@dataclass
class PeriodLogEntryClan:
    tag: str

    @classmethod
    def from_api(cls, data: dict) -> "PeriodLogEntryClan":
        return cls(
            tag=data["tag"]
        )
