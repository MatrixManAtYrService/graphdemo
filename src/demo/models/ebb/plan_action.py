from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalPlanActionMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'plan_action_type',
        'fee_category',
        'fee_code',
        'num_units',
        'units_in_period',
    }

    def to_minimal_dict(self) -> dict:
        return self.model_dump(include=self.MINIMAL_FIELDS)


class PlanAction(BaseModel, MinimalPlanActionMixin):
    """
    Pydantic V2 model for the `plan_action` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the plan action.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    merchant_plan_uuid: str = Field(..., max_length=13, description="UUID of the merchant plan.")
    serial_number: Optional[str] = Field(default=None, max_length=32, description="Serial number, can be null.")
    plan_action_type: str = Field(..., max_length=25, description="Type of plan action.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    action_datetime: datetime.datetime = Field(..., description="Timestamp when the action occurred.")
    num_units: int = Field(default=0, description="Number of units for the action.")
    units_in_period: int = Field(..., description="Number of units within the billing period.", ge=0)
    basis_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="The base amount for calculation."
    )
    basis_currency: Optional[str] = Field(default=None, max_length=3, description="Currency of the basis amount (e.g., USD).")
    reference: Optional[str] = Field(default=None, max_length=50, description="A reference string.")
    plan_action_fee_code_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID for the plan action fee code.")
    fee_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the associated fee.")
    event_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the triggering event.")
    request_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the request that initiated this action.")
    date_to_post: Optional[datetime.date] = Field(default=None, description="The date the action is scheduled to be posted.")
    posting_date: Optional[datetime.date] = Field(default=None, description="The actual date the action was posted.")
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
                "merchant_plan_uuid": "01H8X7Y7Z7QWE",
                "serial_number": "SN123456789",
                "plan_action_type": "SUBSCRIPTION",
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "action_datetime": "2023-10-27T10:00:00.123456",
                "num_units": 1,
                "units_in_period": 1,
                "basis_amount": "99.990",
                "basis_currency": "USD",
                "reference": "Initial Subscription",
                "plan_action_fee_code_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "fee_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGB",
                "event_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGC",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGD",
                "date_to_post": "2023-11-01",
                "posting_date": "2023-11-01",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = PlanAction.model_json_schema().get("example", {})
    plan_action_instance = PlanAction(**example_dict)
    print("----begin example: plan-action----")
    print(plan_action_instance.model_dump_json(indent=2))
    print("----begin minmal example: plan-action----")
    print(json.dumps(plan_action_instance.to_minimal_dict(), indent=2))

    print("----end: plan-action----")
