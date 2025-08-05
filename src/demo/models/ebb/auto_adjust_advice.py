from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalAutoAdjustAdviceMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'total_periods',
        'evaluated_periods',
        'applied_periods',
        'max_units',
        'max_amount',
        'currency',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class AutoAdjustAdvice(BaseModel, MinimalAutoAdjustAdviceMixin):
    """
    Pydantic V2 model for the `auto_adjust_advice` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the auto adjust advice.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    auto_adjust_rule_uuid: str = Field(..., max_length=26, description="UUID of the auto adjust rule.")
    start_date: datetime.date = Field(..., description="Start date for the adjustment.")
    deleted_date: Optional[datetime.date] = Field(default=None, description="Date when the advice was deleted, can be null.")
    total_periods: int = Field(..., description="Total number of periods for the adjustment.")
    evaluated_periods: int = Field(default=0, description="Number of periods that have been evaluated.")
    applied_periods: int = Field(default=0, description="Number of periods where adjustments have been applied.")
    max_units: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=4,
        description="Maximum units for the adjustment."
    )
    max_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Maximum amount for the adjustment."
    )
    currency: Optional[str] = Field(default=None, max_length=3, description="Currency for the adjustment amounts.")
    reference: Optional[str] = Field(default=None, max_length=50, description="A reference string.")
    request_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the request that initiated this advice.")
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
                "auto_adjust_rule_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "start_date": "2023-10-01",
                "deleted_date": None,
                "total_periods": 12,
                "evaluated_periods": 3,
                "applied_periods": 2,
                "max_units": "1000.0000",
                "max_amount": "500.000",
                "currency": "USD",
                "reference": "Annual Volume Discount",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGD",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = AutoAdjustAdvice.model_json_schema().get("example", {})
    auto_adjust_advice_instance = AutoAdjustAdvice(**example_dict)
    print("----begin example: auto-adjust-advice----")
    print(auto_adjust_advice_instance.model_dump_json(indent=2))
    print("----begin minmal example: auto-adjust-advice----")
    print(json.dumps(auto_adjust_advice_instance.to_minimal_dict(), indent=2))

    print("----end: auto-adjust-advice----")