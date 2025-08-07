from __future__ import annotations

import datetime
import json
from typing import Optional, Literal

from pydantic import BaseModel, Field


class MinimalMonetaryAdjustmentMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'rule_type',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class MonetaryAdjustment(BaseModel, MinimalMonetaryAdjustmentMixin):
    """
    Pydantic V2 model for the `monetary_adjustment` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the monetary adjustment.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    adjust_fee_summary_uuid: str = Field(..., max_length=26, description="UUID of the adjustment fee summary.")
    qualified_fee_summary_uuid: str = Field(..., max_length=26, description="UUID of the qualified fee summary.")
    rule_uuid: str = Field(..., max_length=26, description="UUID of the rule.")
    rule_criteria_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the rule criteria.")
    rule_type: Literal["AUTO_ADJUST", "TIERED"] = Field(..., description="Type of rule being applied.")
    request_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the request.")
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "adjust_fee_summary_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "qualified_fee_summary_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGB",
                "rule_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGC",
                "rule_criteria_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGD",
                "rule_type": "AUTO_ADJUST",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGE",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = MonetaryAdjustment.model_json_schema().get("example", {})
    monetary_adjustment_instance = MonetaryAdjustment(**example_dict)
    print("----begin example: monetary-adjustment----")
    print(monetary_adjustment_instance.model_dump_json(indent=2))
    print("----begin minmal example: monetary-adjustment----")
    print(json.dumps(monetary_adjustment_instance.to_minimal_dict(), indent=2))
    print("----end: monetary-adjustment----")