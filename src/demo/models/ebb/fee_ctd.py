from __future__ import annotations

import datetime
import json
from decimal import Decimal

from pydantic import BaseModel, Field


class MinimalFeeCtdMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
        'currency',
        'ctd_num_units',
        'ctd_basis_amount',
        'num_actions',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeCtd(BaseModel, MinimalFeeCtdMixin):
    """
    Pydantic V2 model for the `fee_ctd` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the fee CTD.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    currency: str = Field(..., max_length=3, description="Currency for the amounts.")
    ctd_num_units: Decimal = Field(
        default=Decimal("0.0000"),
        max_digits=12,
        decimal_places=4,
        description="Cycle-to-date number of units."
    )
    abs_num_units: Decimal = Field(
        default=Decimal("0.0000"),
        max_digits=12,
        decimal_places=4,
        description="Absolute number of units."
    )
    ctd_basis_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Cycle-to-date basis amount."
    )
    abs_basis_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Absolute basis amount."
    )
    num_actions: int = Field(default=0, description="Number of actions.")
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
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "currency": "USD",
                "ctd_num_units": "100.0000",
                "abs_num_units": "100.0000",
                "ctd_basis_amount": "2500.000",
                "abs_basis_amount": "2500.000",
                "num_actions": 50,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeCtd.model_json_schema().get("example", {})
    fee_ctd_instance = FeeCtd(**example_dict)
    print("----begin example: fee-ctd----")
    print(fee_ctd_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-ctd----")
    print(json.dumps(fee_ctd_instance.to_minimal_dict(), indent=2))

    print("----end: fee-ctd----")