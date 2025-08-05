from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MutationAction(str, Enum):
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class MinimalInvoiceInfoSettlementMutationMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'mutation_action',
        'mutation_timestamp',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class InvoiceInfoSettlementMutation(BaseModel, MinimalInvoiceInfoSettlementMutationMixin):
    """
    Pydantic V2 model for the `invoice_info_settlement_mutation` table.
    """
    id: int = Field(..., gt=0)
    mutation_action: MutationAction
    mutation_timestamp: datetime.datetime
    invoice_info_settlement_id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    invoice_info_uuid: Optional[str] = Field(default=None, max_length=26)
    settlement_uuid: Optional[str] = Field(default=None, max_length=26)
    request_uuid: Optional[str] = Field(default=None, max_length=26)
    created_timestamp: Optional[datetime.datetime] = Field(default=None)

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                "id": 1,
                "mutation_action": "UPDATE",
                "mutation_timestamp": "2023-10-27T11:00:00.123456",
                "invoice_info_settlement_id": 42,
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "invoice_info_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "settlement_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGY",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = InvoiceInfoSettlementMutation.model_json_schema().get("example", {})
    invoice_info_settlement_mutation_instance = InvoiceInfoSettlementMutation(**example_dict)
    print("----begin example: invoice-info-settlement-mutation----")
    print(invoice_info_settlement_mutation_instance.model_dump_json(indent=2))
    print("----begin minmal example: invoice-info-settlement-mutation----")
    print(json.dumps(invoice_info_settlement_mutation_instance.to_minimal_dict(), indent=2))

    print("----end: invoice-info-settlement-mutation----")