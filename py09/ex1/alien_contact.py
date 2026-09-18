from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact_id must start with AC")

        if not self.is_verified and self.contact_type == ContactType.PHYSICAL:
            raise ValueError("Physical contact reports must be verified")

        if not self.message_received and self.signal_strength > 7.0:
            raise ValueError("Strong signals (> 7.0) should include received messages")  # noqa: E501

        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:  # noqa: E501
            raise ValueError("Telepathic contact requires at least 3 witnesses")  # noqa: E501
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    alien_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2026-10-15T10:30:00"),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="'Greetings from Zeta Reticuli'",
        is_verified=True
    )
    print("valid contact report:")
    print(f"ID: {alien_contact.contact_id}")
    print(f"Type: {alien_contact.contact_type}")
    print(f"Location: {alien_contact.location}")
    print(f"Signal: {alien_contact.signal_strength}")
    print(f"Duration: {alien_contact.duration_minutes}")
    print(f"Witnesses: {alien_contact.witness_count}")
    print(f"Message: {alien_contact.message_received}")
    print("======================================")
    try:
        alien2_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.fromisoformat("2026-10-15T10:30:30"),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="'Greetings from Zeta Reticuli'",
            is_verified=True
        )
        print("valid contact report:")
        print(f"ID: {alien2_contact.contact_id}")
        print(f"Type: {alien2_contact.contact_type}")
        print(f"Location: {alien2_contact.location}")
        print(f"Signal: {alien2_contact.signal_strength}")
        print(f"Duration: {alien2_contact.duration_minutes}")
        print(f"Witnesses: {alien2_contact.witness_count}")
        print(f"Message: {alien2_contact.message_received}")

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
