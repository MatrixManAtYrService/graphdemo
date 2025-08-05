from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalInvoiceAllianceCodeMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'alliance_code',
        'invoice_count',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class InvoiceAllianceCode(BaseModel, MinimalInvoiceAllianceCodeMixin):
    """
    Pydantic V2 model for the `invoice_alliance_code` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    billing_entity_uuid: str = Field(..., max_length=26)
    alliance_code: str = Field(..., max_length=3)
    invoice_count: int = Field(..., gt=0)
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "alliance_code": "VZW",
                "invoice_count": 1001,
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = InvoiceAllianceCode.model_json_schema().get("example", {})
    invoice_alliance_code_instance = InvoiceAllianceCode(**example_dict)
    print("----begin example: invoice-alliance-code----")
    print(invoice_alliance_code_instance.model_dump_json(indent=2))
    print("----begin minmal example: invoice-alliance-code----")
    print(json.dumps(invoice_alliance_code_instance.to_minimal_dict(), indent=2))

    print("----end: invoice-alliance-code----")