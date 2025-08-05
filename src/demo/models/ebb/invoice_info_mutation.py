from __future__ import annotations

import datetime
import json
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MutationAction(str, Enum):
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class MinimalInvoiceInfoMutationMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'mutation_action',
        'billing_date',
        'invoice_num',
        'currency',
        'total_amount',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class InvoiceInfoMutation(BaseModel, MinimalInvoiceInfoMutationMixin):
    """
    Pydantic V2 model for the `invoice_info_mutation` table.
    """
    id: int = Field(..., gt=0)
    mutation_action: MutationAction
    mutation_timestamp: datetime.datetime
    invoice_info_id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    billing_entity_uuid: Optional[str] = Field(default=None, max_length=26)
    entity_uuid: Optional[str] = Field(default=None, max_length=13)
    alternate_id: Optional[str] = Field(default=None, max_length=25)
    billing_date: Optional[datetime.date] = Field(default=None)
    invoice_num: Optional[str] = Field(default=None, max_length=30)
    currency: Optional[str] = Field(default=None, max_length=3)
    total_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3)
    document_uuid: Optional[str] = Field(default=None, max_length=26)
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
                "invoice_info_id": 42,
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "entity_uuid": "01H8X7Y7Z7Q12",
                "alternate_id": "CUST-12345",
                "billing_date": "2023-10-27",
                "invoice_num": "INV-2023-10-001",
                "currency": "USD",
                "total_amount": "149.95",
                "document_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGY",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = InvoiceInfoMutation.model_json_schema().get("example", {})
    invoice_info_mutation_instance = InvoiceInfoMutation(**example_dict)
    print("----begin example: invoice-info-mutation----")
    print(invoice_info_mutation_instance.model_dump_json(indent=2))
    print("----begin minmal example: invoice-info-mutation----")
    print(json.dumps(invoice_info_mutation_instance.to_minimal_dict(), indent=2))

    print("----end: invoice-info-mutation----")