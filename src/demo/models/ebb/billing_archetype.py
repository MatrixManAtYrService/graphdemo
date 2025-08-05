from __future__ import annotations

import datetime
import json
from enum import Enum

from pydantic import BaseModel, Field


class ArchetypeType(str, Enum):
    MERCHANT = "MERCHANT"
    RESELLER = "RESELLER"
    DEVELOPER = "DEVELOPER"
    PSEUDO = "PSEUDO"


class MinimalBillingArchetypeMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'archetype_type',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingArchetype(BaseModel, MinimalBillingArchetypeMixin):
    """
    Pydantic V2 model for the `billing_archetype` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=13, description="Unique identifier for the billing archetype.")
    archetype_type: ArchetypeType = Field(..., description="Type of archetype.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                "id": 1,
                "uuid": "01H8X7Y7Z7QWE",
                "archetype_type": "MERCHANT",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = BillingArchetype.model_json_schema().get("example", {})
    billing_archetype_instance = BillingArchetype(**example_dict)
    print("----begin example: billing-archetype----")
    print(billing_archetype_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-archetype----")
    print(json.dumps(billing_archetype_instance.to_minimal_dict(), indent=2))

    print("----end: billing-archetype----")