from dataclasses import dataclass

from . import PeriodLogEntry


@dataclass
class PeriodLog:
    items: list[PeriodLogEntry]
    period_index: int

    @classmethod
    def from_api(cls, data: dict) -> "PeriodLog":
        return cls(
            items=[PeriodLogEntry.from_api(item) for item in data["items"]],
            period_index=data["periodIndex"]
        )
