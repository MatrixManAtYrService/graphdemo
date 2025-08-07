from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalTieredQualifierMixin:

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


class TieredQualifier(BaseModel, MinimalTieredQualifierMixin):
    """
    Pydantic V2 model for the `tiered_qualifier` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the tiered qualifier.")
    tiered_rule_uuid: str = Field(..., max_length=26, description="UUID of the tiered rule.")
    fee_category: str = Field(..., max_length=25, description="Fee category for qualification.")
    fee_code: str = Field(..., max_length=25, description="Fee code for qualification.")
    negate_fee_summary: int = Field(default=0, description="Whether to negate fee summary (0/1).")
    disqualify: int = Field(default=0, description="Whether this disqualifies (0/1).")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    audit_id: Optional[str] = Field(default=None, max_length=26, description="Audit identifier.")

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
                "tiered_rule_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "fee_category": "TRANSACTION",
                "fee_code": "PAYMENT_FEE",
                "negate_fee_summary": 0,
                "disqualify": 0,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = TieredQualifier.model_json_schema().get("example", {})
    tiered_qualifier_instance = TieredQualifier(**example_dict)
    print("----begin example: tiered-qualifier----")
    print(tiered_qualifier_instance.model_dump_json(indent=2))
    print("----begin minmal example: tiered-qualifier----")
    print(json.dumps(tiered_qualifier_instance.to_minimal_dict(), indent=2))
    print("----end: tiered-qualifier----")