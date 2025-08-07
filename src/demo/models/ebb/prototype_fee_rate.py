from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional, Literal

from pydantic import BaseModel, Field


class MinimalPrototypeFeeRateMixin:

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
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class PrototypeFeeRate(BaseModel, MinimalPrototypeFeeRateMixin):
    """
    Pydantic V2 model for the `prototype_fee_rate` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the prototype fee rate.")
    prototype_fee_set_id: int = Field(..., description="ID of the prototype fee set.", gt=0)
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    currency: str = Field(..., max_length=3, description="Currency code (e.g., USD).")
    apply_type: Literal["DEFAULT", "PER_ITEM", "PERCENTAGE", "BOTH", "NONE", "FLAT"] = Field(
        ..., description="How the fee rate is applied."
    )
    per_item_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Per-item fee amount."
    )
    percentage: Optional[Decimal] = Field(
        default=None,
        max_digits=5,
        decimal_places=2,
        description="Percentage rate for fee calculation."
    )
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
                "prototype_fee_set_id": 123,
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "fee_category": "TRANSACTION",
                "fee_code": "PAYMENT_FEE",
                "currency": "USD",
                "apply_type": "PERCENTAGE",
                "per_item_amount": None,
                "percentage": "2.50",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = PrototypeFeeRate.model_json_schema().get("example", {})
    prototype_fee_rate_instance = PrototypeFeeRate(**example_dict)
    print("----begin example: prototype-fee-rate----")
    print(prototype_fee_rate_instance.model_dump_json(indent=2))
    print("----begin minmal example: prototype-fee-rate----")
    print(json.dumps(prototype_fee_rate_instance.to_minimal_dict(), indent=2))
    print("----end: prototype-fee-rate----")