from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalInvoiceInfoAmountMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'currency',
        'amount',
        'fee_category_group',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class InvoiceInfoAmount(BaseModel, MinimalInvoiceInfoAmountMixin):
    """
    Pydantic V2 model for the `invoice_info_amount` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    invoice_info_uuid: str = Field(..., max_length=26)
    currency: str = Field(..., max_length=3)
    amount: Decimal = Field(..., max_digits=12, decimal_places=3)
    fee_category_group: str = Field(..., max_length=25)
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
                "invoice_info_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "currency": "USD",
                "amount": "29.990",
                "fee_category_group": "RECURRING_FEES",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = InvoiceInfoAmount.model_json_schema().get("example", {})
    invoice_info_amount_instance = InvoiceInfoAmount(**example_dict)
    print("----begin example: invoice-info-amount----")
    print(invoice_info_amount_instance.model_dump_json(indent=2))
    print("----begin minmal example: invoice-info-amount----")
    print(json.dumps(invoice_info_amount_instance.to_minimal_dict(), indent=2))

    print("----end: invoice-info-amount----")