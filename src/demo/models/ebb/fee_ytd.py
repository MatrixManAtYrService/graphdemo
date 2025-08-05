from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalFeeYtdMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'year',
        'fee_category',
        'fee_code',
        'currency',
        'total_fee_amount',
        'total_period_units',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeYtd(BaseModel, MinimalFeeYtdMixin):
    """
    Pydantic V2 model for the `fee_ytd` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    billing_entity_uuid: str = Field(..., max_length=26)
    year: int
    fee_category: str = Field(..., max_length=25)
    fee_code: str = Field(..., max_length=25)
    currency: str = Field(..., max_length=3)
    total_period_units: Decimal = Field(..., max_digits=12, decimal_places=4)
    total_basis_amount: Decimal = Field(..., max_digits=12, decimal_places=3)
    total_fee_amount: Decimal = Field(..., max_digits=12, decimal_places=3)
    created_timestamp: datetime.datetime
    modified_timestamp: datetime.datetime

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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "year": 2023,
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "currency": "USD",
                "total_period_units": "12.0000",
                "total_basis_amount": "359.880",
                "total_fee_amount": "359.880",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeYtd.model_json_schema().get("example", {})
    fee_ytd_instance = FeeYtd(**example_dict)
    print("----begin example: fee-ytd----")
    print(fee_ytd_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-ytd----")
    print(json.dumps(fee_ytd_instance.to_minimal_dict(), indent=2))

    print("----end: fee-ytd----")