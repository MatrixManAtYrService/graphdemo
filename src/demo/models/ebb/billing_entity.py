from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class EntityType(str, Enum):
    MERCHANT = "MERCHANT"
    RESELLER = "RESELLER"
    DEVELOPER = "DEVELOPER"
    PSEUDO = "PSEUDO"
    ARCHETYPE = "ARCHETYPE"


class MinimalBillingEntityMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'entity_type',
        'name',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingEntity(BaseModel, MinimalBillingEntityMixin):
    """
    Pydantic V2 model for the `billing_entity` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the billing entity.")
    entity_uuid: str = Field(..., max_length=13, description="UUID of the entity.")
    entity_type: EntityType = Field(..., description="Type of entity.")
    name: Optional[str] = Field(default=None, max_length=127, description="Name of the entity, can be null.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
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
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "entity_uuid": "01H8X7Y7Z7QWE",
                "entity_type": "MERCHANT",
                "name": "Acme Corporation",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = BillingEntity.model_json_schema().get("example", {})
    billing_entity_instance = BillingEntity(**example_dict)
    print("----begin example: billing-entity----")
    print(billing_entity_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-entity----")
    print(json.dumps(billing_entity_instance.to_minimal_dict(), indent=2))

    print("----end: billing-entity----")