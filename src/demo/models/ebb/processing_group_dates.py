from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalProcessingGroupDatesMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'hierarchy_type',
        'cycle_date',
        'posting_date',
        'billing_date',
        'settlement_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class ProcessingGroupDates(BaseModel, MinimalProcessingGroupDatesMixin):
    """
    Pydantic V2 model for the `processing_group_dates` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the processing group dates.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    hierarchy_type: str = Field(..., max_length=20, description="Type of billing hierarchy.")
    cycle_date: datetime.date = Field(..., description="Current cycle date.")
    last_cycle_date: Optional[datetime.date] = Field(default=None, description="Previous cycle date.")
    posting_date: datetime.date = Field(..., description="Current posting date.")
    last_posting_date: Optional[datetime.date] = Field(default=None, description="Previous posting date.")
    billing_date: datetime.date = Field(..., description="Current billing date.")
    last_billing_date: Optional[datetime.date] = Field(default=None, description="Previous billing date.")
    settlement_date: datetime.date = Field(..., description="Current settlement date.")
    last_settlement_date: Optional[datetime.date] = Field(default=None, description="Previous settlement date.")
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
                "hierarchy_type": "MERCHANT",
                "cycle_date": "2023-11-01",
                "last_cycle_date": "2023-10-01",
                "posting_date": "2023-11-02",
                "last_posting_date": "2023-10-02",
                "billing_date": "2023-11-03",
                "last_billing_date": "2023-10-03",
                "settlement_date": "2023-11-15",
                "last_settlement_date": "2023-10-15",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = ProcessingGroupDates.model_json_schema().get("example", {})
    processing_group_dates_instance = ProcessingGroupDates(**example_dict)
    print("----begin example: processing-group-dates----")
    print(processing_group_dates_instance.model_dump_json(indent=2))
    print("----begin minmal example: processing-group-dates----")
    print(json.dumps(processing_group_dates_instance.to_minimal_dict(), indent=2))
    print("----end: processing-group-dates----")