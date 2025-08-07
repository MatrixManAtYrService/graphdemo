from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional, Literal

from pydantic import BaseModel, Field


class MinimalSettlementMutationMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'mutation_action',
        'payable_receivable',
        'currency',
        'total_amount',
        'fee_amount',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class SettlementMutation(BaseModel, MinimalSettlementMutationMixin):
    """
    Pydantic V2 model for the `settlement_mutation` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    mutation_action: Literal["UPDATE", "DELETE"] = Field(..., description="Type of mutation action.")
    mutation_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the mutation occurred."
    )
    settlement_id: int = Field(..., description="ID of the settlement record.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the settlement.")
    settlement_date: Optional[datetime.date] = Field(default=None, description="Date of the settlement.")
    billing_entity_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the billing entity.")
    entity_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the entity.")
    alternate_id: Optional[str] = Field(default=None, max_length=30, description="Alternate identifier.")
    payable_receivable: Optional[Literal["PAYABLE", "RECEIVABLE"]] = Field(default=None, description="Whether this is payable or receivable.")
    currency: Optional[str] = Field(default=None, max_length=3, description="Currency code (e.g., USD).")
    total_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Total settlement amount."
    )
    fee_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Fee amount."
    )
    tax1_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Tax 1 amount."
    )
    tax2_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Tax 2 amount."
    )
    tax3_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Tax 3 amount."
    )
    tax4_amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Tax 4 amount."
    )
    lookup_ledger_account_key: Optional[str] = Field(default=None, max_length=32, description="Ledger account lookup key.")
    gl_code: Optional[str] = Field(default=None, max_length=40, description="General ledger code.")
    item_code: Optional[str] = Field(default=None, max_length=30, description="Item code.")
    last_invoice_num: Optional[str] = Field(default=None, max_length=30, description="Last invoice number.")
    request_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the request.")
    created_timestamp: Optional[datetime.datetime] = Field(default=None, description="Timestamp when the original record was created.")
    modified_timestamp: Optional[datetime.datetime] = Field(default=None, description="Timestamp when the original record was last modified.")

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
                "settlement_id": 123,
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "settlement_date": "2023-11-01",
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "entity_uuid": "01H8X7Y7Z7QWE",
                "alternate_id": "SETTLE-2023-001",
                "payable_receivable": "PAYABLE",
                "currency": "USD",
                "total_amount": "1234.567",
                "fee_amount": "123.456",
                "tax1_amount": "12.345",
                "tax2_amount": "0.000",
                "tax3_amount": "0.000",
                "tax4_amount": "0.000",
                "lookup_ledger_account_key": "MERCHANT_PAYABLE_USD",
                "gl_code": "2100-001",
                "item_code": "MERCHANT_FEE",
                "last_invoice_num": "INV-2023-001234",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = SettlementMutation.model_json_schema().get("example", {})
    settlement_mutation_instance = SettlementMutation(**example_dict)
    print("----begin example: settlement-mutation----")
    print(settlement_mutation_instance.model_dump_json(indent=2))
    print("----begin minmal example: settlement-mutation----")
    print(json.dumps(settlement_mutation_instance.to_minimal_dict(), indent=2))
    print("----end: settlement-mutation----")