from __future__ import annotations

import datetime
import json

from pydantic import BaseModel, Field


class MinimalAdjustReasonMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'adjust_reason',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class AdjustReason(BaseModel, MinimalAdjustReasonMixin):
    """
    Pydantic V2 model for the `adjust_reason` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the adjust reason.")
    adjust_reason: str = Field(..., max_length=25, description="Reason for the adjustment.")
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
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "adjust_reason": "REFUND",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = AdjustReason.model_json_schema().get("example", {})
    adjust_reason_instance = AdjustReason(**example_dict)
    print("----begin example: adjust-reason----")
    print(adjust_reason_instance.model_dump_json(indent=2))
    print("----begin minmal example: adjust-reason----")
    print(json.dumps(adjust_reason_instance.to_minimal_dict(), indent=2))

    print("----end: adjust-reason----")