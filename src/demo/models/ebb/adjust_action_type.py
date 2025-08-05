from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalAdjustActionTypeMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'adjust_action_type',
        'fee_category_group',
        'revenue_group',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class AdjustActionType(BaseModel, MinimalAdjustActionTypeMixin):
    """
    Pydantic V2 model for the `adjust_action_type` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the adjust action type.")
    adjust_action_type: str = Field(..., max_length=25, description="Type of adjustment action.")
    fee_category_group: str = Field(..., max_length=25, description="Group of fee categories.")
    revenue_group: Optional[str] = Field(default=None, max_length=25, description="Revenue group, can be null.")
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
                "adjust_action_type": "CREDIT_ADJUSTMENT",
                "fee_category_group": "RECURRING_FEES",
                "revenue_group": "SUBSCRIPTION_REVENUE",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = AdjustActionType.model_json_schema().get("example", {})
    adjust_action_type_instance = AdjustActionType(**example_dict)
    print("----begin example: adjust-action-type----")
    print(adjust_action_type_instance.model_dump_json(indent=2))
    print("----begin minmal example: adjust-action-type----")
    print(json.dumps(adjust_action_type_instance.to_minimal_dict(), indent=2))

    print("----end: adjust-action-type----")