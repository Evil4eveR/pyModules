from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    validtest = SpaceStation(
        station_id="42WOLF",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.fromisoformat("2024-01-15T10:00:00"),
        notes="All systems nominal"
    )
    print("Valid station created:")
    print("ID:", validtest.station_id)
    print("Name:", validtest.name)
    print(f"Crew: {validtest.crew_size} people")
    print(f"Power: {validtest.power_level}%")
    print(f"Oxygen: {validtest.oxygen_level}%")
    print(f"Status: {'Operational' if validtest.is_operational else 'Offline'}")  # noqa E501
    print("========================================")
    try:
        invalidtest = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=75,
            power_level=77.77,
            oxygen_level=8.1,
            last_maintenance=datetime.fromisoformat("2024-01-15T10:00:59"),
            notes="great Vibe"
        )
        print(invalidtest)

    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
