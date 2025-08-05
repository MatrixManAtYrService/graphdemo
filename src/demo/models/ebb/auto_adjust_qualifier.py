from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalAutoAdjustQualifierMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
        'negate_fee_summary',
        'disqualify',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class AutoAdjustQualifier(BaseModel, MinimalAutoAdjustQualifierMixin):
    """
    Pydantic V2 model for the `auto_adjust_qualifier` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the auto adjust qualifier.")
    auto_adjust_rule_uuid: str = Field(..., max_length=26, description="UUID of the auto adjust rule.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    negate_fee_summary: int = Field(default=0, description="Whether to negate the fee summary (0/1).")
    disqualify: int = Field(default=0, description="Whether this qualifier disqualifies the rule (0/1).")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    audit_id: Optional[str] = Field(default=None, max_length=26, description="Audit identifier, can be null.")

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
                "auto_adjust_rule_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "negate_fee_summary": 0,
                "disqualify": 0,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = AutoAdjustQualifier.model_json_schema().get("example", {})
    auto_adjust_qualifier_instance = AutoAdjustQualifier(**example_dict)
    print("----begin example: auto-adjust-qualifier----")
    print(auto_adjust_qualifier_instance.model_dump_json(indent=2))
    print("----begin minmal example: auto-adjust-qualifier----")
    print(json.dumps(auto_adjust_qualifier_instance.to_minimal_dict(), indent=2))

    print("----end: auto-adjust-qualifier----")