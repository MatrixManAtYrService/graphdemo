from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Frequency(str, Enum):
    NO_BILL = "NO_BILL"
    MONTHLY = "MONTHLY"


class MinimalBillingScheduleMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'frequency',
        'billing_day',
        'next_billing_date',
        'units_in_next_period',
        'default_currency',
        'effective_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingSchedule(BaseModel, MinimalBillingScheduleMixin):
    """
    Pydantic V2 model for the `billing_schedule` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the billing schedule.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    effective_date: datetime.date = Field(..., description="Date when the schedule becomes effective.")
    frequency: Frequency = Field(..., description="Billing frequency.")
    billing_day: int = Field(..., description="Day of the month for billing.")
    next_billing_date: datetime.date = Field(..., description="Next billing date.")
    last_billing_date: Optional[datetime.date] = Field(default=None, description="Last billing date, can be null.")
    units_in_next_period: int = Field(..., description="Units in the next billing period.")
    units_in_last_period: Optional[int] = Field(default=None, description="Units in the last billing period, can be null.")
    default_currency: str = Field(..., max_length=3, description="Default currency for billing.")
    close_date: Optional[datetime.date] = Field(default=None, description="Date when the schedule was closed, can be null.")
    effective_close_date: Optional[datetime.date] = Field(default=None, description="Effective close date, can be null.")
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "effective_date": "2023-10-01",
                "frequency": "MONTHLY",
                "billing_day": 1,
                "next_billing_date": "2023-11-01",
                "last_billing_date": "2023-10-01",
                "units_in_next_period": 1,
                "units_in_last_period": 1,
                "default_currency": "USD",
                "close_date": None,
                "effective_close_date": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = BillingSchedule.model_json_schema().get("example", {})
    billing_schedule_instance = BillingSchedule(**example_dict)
    print("----begin example: billing-schedule----")
    print(billing_schedule_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-schedule----")
    print(json.dumps(billing_schedule_instance.to_minimal_dict(), indent=2))

    print("----end: billing-schedule----")