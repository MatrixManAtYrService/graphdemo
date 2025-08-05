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


class MinimalBillingEventHistoryMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'environment',
        'entity_type',
        'message',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingEventHistory(BaseModel, MinimalBillingEventHistoryMixin):
    """
    Pydantic V2 model for the `billing_event_history` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    environment: str = Field(..., max_length=25, description="Environment where the event occurred.")
    entity_uuid: str = Field(..., max_length=13, description="UUID of the entity.")
    entity_type: EntityType = Field(..., description="Type of entity.")
    event_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the event, can be null.")
    input: str = Field(..., description="Input data for the event.")
    message: Optional[str] = Field(default=None, max_length=1024, description="Event message, can be null.")
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
                "environment": "PRODUCTION",
                "entity_uuid": "01H8X7Y7Z7QWE",
                "entity_type": "MERCHANT",
                "event_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "input": '{"action": "create_invoice", "amount": 99.99}',
                "message": "Invoice created successfully",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = BillingEventHistory.model_json_schema().get("example", {})
    billing_event_history_instance = BillingEventHistory(**example_dict)
    print("----begin example: billing-event-history----")
    print(billing_event_history_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-event-history----")
    print(json.dumps(billing_event_history_instance.to_minimal_dict(), indent=2))

    print("----end: billing-event-history----")