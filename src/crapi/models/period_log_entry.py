from dataclasses import dataclass

from . import PeriodLogEntryClan


@dataclass
class PeriodLogEntry:
    clan: PeriodLogEntryClan
    points_earned: int
    progress_start_of_day: int
    progress_end_of_day: int
    end_of_day_rank: int
    progress_earned: int
    num_of_defenses_remaining: int
    progress_earned_from_defenses: int

    @classmethod
    def from_api(cls, data: dict) -> "PeriodLogEntry":
        return cls(
            clan=PeriodLogEntryClan.from_api(data["clan"]),
            points_earned=int(data["points_earned"]),
            progress_start_of_day=int(data["progress_start_of_day"]),
            progress_end_of_day=int(data["progress_end_of_day"]),
            end_of_day_rank=int(data["end_of_day_rank"]),
            progress_earned=int(data["progress_earned"]),
            num_of_defenses_remaining=int(data["num_of_defenses_remaining"]),
            progress_earned_from_defenses=int(data["progress_earned_from_defenses"])
        )
