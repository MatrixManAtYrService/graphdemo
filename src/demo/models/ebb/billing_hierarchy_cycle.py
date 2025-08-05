from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Frequency(str, Enum):
    NO_BILL = "NO_BILL"
    MONTHLY = "MONTHLY"


class MinimalBillingHierarchyCycleMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'frequency',
        'billing_day',
        'next_billing_date',
        'default_currency',
        'post_method',
        'plan_billing_method',
        'invoice_method',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingHierarchyCycle(BaseModel, MinimalBillingHierarchyCycleMixin):
    """
    Pydantic V2 model for the `billing_hierarchy_cycle` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the billing hierarchy cycle.")
    processing_group_uuid: str = Field(..., max_length=26, description="UUID of the processing group.")
    billing_hierarchy_uuid: str = Field(..., max_length=26, description="UUID of the billing hierarchy.")
    cycle_date: datetime.date = Field(..., description="Date of the billing cycle.")
    close_date: Optional[datetime.date] = Field(default=None, description="Date when the cycle was closed, can be null.")
    effective_close_date: Optional[datetime.date] = Field(default=None, description="Effective close date, can be null.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    entity_uuid: str = Field(..., max_length=13, description="UUID of the entity.")
    schedule_parent_be_uuid: str = Field(..., max_length=26, description="UUID of the schedule parent billing entity.")
    fee_rate_parent_be_uuid: str = Field(..., max_length=26, description="UUID of the fee rate parent billing entity.")
    frequency: Frequency = Field(..., description="Billing frequency.")
    billing_day: int = Field(..., description="Day of the month for billing.")
    next_billing_date: datetime.date = Field(..., description="Next billing date.")
    last_billing_date: Optional[datetime.date] = Field(default=None, description="Last billing date, can be null.")
    arrears_billing_date: Optional[datetime.date] = Field(default=None, description="Arrears billing date, can be null.")
    units_in_next_period: int = Field(..., description="Units in the next billing period.")
    units_in_last_period: Optional[int] = Field(default=None, description="Units in the last billing period, can be null.")
    units_in_arrears_period: Optional[int] = Field(default=None, description="Units in the arrears period, can be null.")
    default_currency: str = Field(..., max_length=3, description="Default currency for billing.")
    post_method: str = Field(..., max_length=20, description="Method for posting.")
    plan_billing_method: str = Field(..., max_length=20, description="Method for plan billing.")
    invoice_method: str = Field(..., max_length=20, description="Method for invoicing.")
    invoice_number_format: str = Field(..., max_length=20, description="Format for invoice numbers.")
    settlement_method: str = Field(..., max_length=20, description="Method for settlement.")
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
                "processing_group_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "billing_hierarchy_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "cycle_date": "2023-10-01",
                "close_date": "2023-10-31",
                "effective_close_date": "2023-10-31",
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGW",
                "entity_uuid": "01H8X7Y7Z7QWE",
                "schedule_parent_be_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGV",
                "fee_rate_parent_be_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGU",
                "frequency": "MONTHLY",
                "billing_day": 1,
                "next_billing_date": "2023-11-01",
                "last_billing_date": "2023-10-01",
                "arrears_billing_date": None,
                "units_in_next_period": 1,
                "units_in_last_period": 1,
                "units_in_arrears_period": None,
                "default_currency": "USD",
                "post_method": "AUTOMATIC",
                "plan_billing_method": "MONTHLY",
                "invoice_method": "EMAIL",
                "invoice_number_format": "INV-{YY}-{MM}-{NNN}",
                "settlement_method": "NET30",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = BillingHierarchyCycle.model_json_schema().get("example", {})
    billing_hierarchy_cycle_instance = BillingHierarchyCycle(**example_dict)
    print("----begin example: billing-hierarchy-cycle----")
    print(billing_hierarchy_cycle_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-hierarchy-cycle----")
    print(json.dumps(billing_hierarchy_cycle_instance.to_minimal_dict(), indent=2))

    print("----end: billing-hierarchy-cycle----")