from __future__ import annotations

import datetime
import json
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ApplyType(str, Enum):
    DEFAULT = "DEFAULT"
    PER_ITEM = "PER_ITEM"
    PERCENTAGE = "PERCENTAGE"
    BOTH = "BOTH"
    NONE = "NONE"
    FLAT = "FLAT"


class MinimalFeeRateMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
        'currency',
        'apply_type',
        'per_item_amount',
        'percentage',
        'effective_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeRate(BaseModel, MinimalFeeRateMixin):
    """
    Pydantic V2 model for the `fee_rate` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the fee rate.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    currency: str = Field(..., max_length=3, description="Currency for the rate.")
    effective_date: datetime.date = Field(..., description="Date when the rate becomes effective.")
    apply_type: ApplyType = Field(..., description="How the rate is applied.")
    per_item_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Per-item amount, can be null."
    )
    percentage: Optional[Decimal] = Field(
        default=None,
        max_digits=5,
        decimal_places=2,
        description="Percentage rate, can be null."
    )
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "currency": "USD",
                "effective_date": "2023-10-01",
                "apply_type": "PER_ITEM",
                "per_item_amount": "29.990",
                "percentage": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = FeeRate.model_json_schema().get("example", {})
    fee_rate_instance = FeeRate(**example_dict)
    print("----begin example: fee-rate----")
    print(fee_rate_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-rate----")
    print(json.dumps(fee_rate_instance.to_minimal_dict(), indent=2))

    print("----end: fee-rate----")