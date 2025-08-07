from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalSettlementActionMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'action_date',
        'action',
        'currency',
        'total_amount',
        'fee_amount',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class SettlementAction(BaseModel, MinimalSettlementActionMixin):
    """
    Pydantic V2 model for the `settlement_action` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the settlement action.")
    settlement_uuid: str = Field(..., max_length=26, description="UUID of the settlement.")
    action_date: datetime.date = Field(..., description="Date of the action.")
    action: str = Field(..., max_length=25, description="Type of action.")
    currency: str = Field(..., max_length=3, description="Currency code (e.g., USD).")
    total_amount: Decimal = Field(
        ...,
        max_digits=12,
        decimal_places=3,
        description="Total action amount."
    )
    fee_amount: Decimal = Field(
        ...,
        max_digits=12,
        decimal_places=3,
        description="Fee amount."
    )
    tax1_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Tax 1 amount."
    )
    tax2_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Tax 2 amount."
    )
    tax3_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Tax 3 amount."
    )
    tax4_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Tax 4 amount."
    )
    reject_code: Optional[str] = Field(default=None, max_length=10, description="Rejection code if applicable.")
    message: Optional[str] = Field(default=None, max_length=1024, description="Action message or details.")
    ledger_account_transition_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of ledger account transition.")
    credit_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of credit ledger account.")
    debit_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of debit ledger account.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
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
                "settlement_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "action_date": "2023-11-01",
                "action": "PAYMENT",
                "currency": "USD",
                "total_amount": "1234.567",
                "fee_amount": "123.456",
                "tax1_amount": "12.345",
                "tax2_amount": "0.000",
                "tax3_amount": "0.000",
                "tax4_amount": "0.000",
                "reject_code": None,
                "message": "Payment processed successfully",
                "ledger_account_transition_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "credit_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGB",
                "debit_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGC",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = SettlementAction.model_json_schema().get("example", {})
    settlement_action_instance = SettlementAction(**example_dict)
    print("----begin example: settlement-action----")
    print(settlement_action_instance.model_dump_json(indent=2))
    print("----begin minmal example: settlement-action----")
    print(json.dumps(settlement_action_instance.to_minimal_dict(), indent=2))
    print("----end: settlement-action----")