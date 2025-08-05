from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalInvoiceInfoSettlementMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'created_timestamp',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class InvoiceInfoSettlement(BaseModel, MinimalInvoiceInfoSettlementMixin):
    """
    Pydantic V2 model for the `invoice_info_settlement` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    invoice_info_uuid: str = Field(..., max_length=26)
    settlement_uuid: str = Field(..., max_length=26)
    request_uuid: str = Field(..., max_length=26)
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
                "settlement_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGY",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = InvoiceInfoSettlement.model_json_schema().get("example", {})
    invoice_info_settlement_instance = InvoiceInfoSettlement(**example_dict)
    print("----begin example: invoice-info-settlement----")
    print(invoice_info_settlement_instance.model_dump_json(indent=2))
    print("----begin minmal example: invoice-info-settlement----")
    print(json.dumps(invoice_info_settlement_instance.to_minimal_dict(), indent=2))

    print("----end: invoice-info-settlement----")