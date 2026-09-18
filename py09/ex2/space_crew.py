from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status:  str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        lead_counter: int = 0
        for crw in self.crew:
            if crw.rank == Rank.CAPTAIN or crw.rank == Rank.COMMANDER:
                lead_counter += 1
        if lead_counter == 0:
            raise ValueError("Crew Must have at least one Commander or Captain")  # noqa: E501

        if (self.duration_days > 365):
            crw_exp_counter = 0
            for crw in self.crew:
                if crw.years_experience >= 5:
                    crw_exp_counter += 1
            if crw_exp_counter < len(self.crew)/2:
                raise ValueError("Long missions (> 365 days) need 50% experienced crew (5+ years)")  # noqa: E501

        for crw in self.crew:
            if not crw.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("======================================")
    crew_42: list[CrewMember] = [
                CrewMember(
                    member_id="WOLF001",
                    name="Yassin",
                    rank=Rank.LIEUTENANT,
                    age=29,
                    specialization="Navigation",
                    years_experience=3,
                ),
                CrewMember(
                    member_id="WOLF002",
                    name="Karim",
                    rank=Rank.CAPTAIN,
                    age=20,
                    specialization="Mission Command",
                    years_experience=5,
                ),
                CrewMember(
                    member_id="WOLF003",
                    name="Denis",
                    rank=Rank.OFFICER,
                    age=25,
                    specialization="Engineering",
                    years_experience=8,
                )
            ]
    mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2024-06-01T06:00:00"),
            duration_days=900,
            crew=crew_42,
            budget_millions=2500.0,
            )
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in crew_42:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")

    print("======================================")
    try:
        failed_crew: list[CrewMember] = [
                    CrewMember(
                        member_id="WOLF001",
                        name="bot1",
                        rank=Rank.LIEUTENANT,
                        age=29,
                        specialization="Navigation",
                        years_experience=3,
                    ),
                    CrewMember(
                        member_id="WOLF002",
                        name="bot5",
                        rank=Rank.CADET,
                        age=20,
                        specialization="Mission Command",
                        years_experience=5,
                    ),
                    CrewMember(
                        member_id="WOLF003",
                        name="bot3",
                        rank=Rank.COMMANDER,
                        age=25,
                        specialization="Engineering",
                        years_experience=8
                    )
                ]
        failed_mission = SpaceMission(
                    mission_id="2024_MARS",
                    mission_name="Mars Colony Establishment",
                    destination="Mars",
                    launch_date=datetime.fromisoformat("2024-06-01T06:00:00"),
                    duration_days=900,
                    crew=failed_crew,
                    budget_millions=2500.0,
                    )
        print("Valid mission created:")
        print(f"Mission: {failed_mission.mission_name}")
        print(f"ID: {failed_mission.mission_id}")
        print(f"Destination: {failed_mission.destination}")
        print(f"Duration: {failed_mission.duration_days} days")
        print(f"Budget: ${failed_mission.budget_millions}M")
        print(f"Crew size: {len(failed_mission.crew)}")
        print("Crew members:")
        for member in failed_crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
