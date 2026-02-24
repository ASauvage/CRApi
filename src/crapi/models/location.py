from dataclasses import dataclass


@dataclass
class Location:
    id: int
    name: str
    localized_name: str
    is_country: bool
    country_code: str | None

    @classmethod
    def from_api(cls, data: dict) -> "Location":
        return cls(
            id=int(data["id"]),
            name=data["name"],
            localized_name=data["localizedName"],
            is_country=data["isCountry"],
            country_code=data["countryCode"] if data["isCountry"] else None
        )
