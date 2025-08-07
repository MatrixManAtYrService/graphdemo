from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalTierDetailMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'min_units',
        'min_amount',
        'currency',
        'rate_fee_category',
        'rate_fee_code',
        'short_desc',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class TierDetail(BaseModel, MinimalTierDetailMixin):
    """
    Pydantic V2 model for the `tier_detail` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the tier detail.")
    tiered_rule_uuid: str = Field(..., max_length=26, description="UUID of the tiered rule.")
    min_units: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=4,
        description="Minimum units for this tier."
    )
    min_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Minimum amount for this tier."
    )
    currency: Optional[str] = Field(default=None, max_length=3, description="Currency code (e.g., USD).")
    rate_fee_category: str = Field(..., max_length=25, description="Rate fee category.")
    rate_fee_code: str = Field(..., max_length=25, description="Rate fee code.")
    short_desc: str = Field(..., max_length=40, description="Short description of the tier.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
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
                "min_units": "1000.0000",
                "min_amount": "100.000",
                "currency": "USD",
                "rate_fee_category": "VOLUME_DISCOUNT",
                "rate_fee_code": "TIER_1_DISCOUNT",
                "short_desc": "Tier 1: 1000+ units",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = TierDetail.model_json_schema().get("example", {})
    tier_detail_instance = TierDetail(**example_dict)
    print("----begin example: tier-detail----")
    print(tier_detail_instance.model_dump_json(indent=2))
    print("----begin minmal example: tier-detail----")
    print(json.dumps(tier_detail_instance.to_minimal_dict(), indent=2))
    print("----end: tier-detail----")