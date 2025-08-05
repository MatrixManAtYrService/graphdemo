from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalFeeTaxMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'tax1_amount',
        'tax2_amount',
        'tax1_rate',
        'tax2_rate',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeTax(BaseModel, MinimalFeeTaxMixin):
    """
    Pydantic V2 model for the `fee_tax` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    fee_summary_uuid: str = Field(..., max_length=26)
    tax1_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3)
    tax2_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3)
    tax3_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3)
    tax4_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3)
    tax1_rate: Optional[Decimal] = Field(default=None, max_digits=7, decimal_places=4)
    tax2_rate: Optional[Decimal] = Field(default=None, max_digits=7, decimal_places=4)
    tax3_rate: Optional[Decimal] = Field(default=None, max_digits=7, decimal_places=4)
    tax4_rate: Optional[Decimal] = Field(default=None, max_digits=7, decimal_places=4)
    created_timestamp: datetime.datetime

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
                "fee_summary_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "tax1_amount": "2.400",
                "tax2_amount": "1.800",
                "tax3_amount": None,
                "tax4_amount": None,
                "tax1_rate": "0.0800",
                "tax2_rate": "0.0600",
                "tax3_rate": None,
                "tax4_rate": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeTax.model_json_schema().get("example", {})
    fee_tax_instance = FeeTax(**example_dict)
    print("----begin example: fee-tax----")
    print(fee_tax_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-tax----")
    print(json.dumps(fee_tax_instance.to_minimal_dict(), indent=2))

    print("----end: fee-tax----")