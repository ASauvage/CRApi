from dataclasses import dataclass


@dataclass
class ClanWarParticipant:
    tag: str
    name: str
    cards_earned: int
    battles_played: int
    collection_day_battles_played: int
    wins: int
    number_of_battles: int

    @classmethod
    def from_api(cls, data: dict) -> "ClanWarParticipant":
        return cls(
            tag=data["tag"],
            name=data["name"],
            cards_earned=data["cardsEarned"],
            battles_played=data["battlesPlayed"],
            collection_day_battles_played=data["collectionDayBattlesPlayed"],
            wins=data["wins"],
            number_of_battles=data["numberOfBattles"]
        )
