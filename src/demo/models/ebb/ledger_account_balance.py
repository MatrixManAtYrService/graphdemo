from __future__ import annotations

import datetime
import json
from decimal import Decimal

from pydantic import BaseModel, Field


class MinimalLedgerAccountBalanceMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'currency',
        'balance',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerAccountBalance(BaseModel, MinimalLedgerAccountBalanceMixin):
    """
    Pydantic V2 model for the `ledger_account_balance` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    ledger_account_uuid: str = Field(..., max_length=26)
    currency: str = Field(..., max_length=3)
    balance: Decimal = Field(..., max_digits=12, decimal_places=3)
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
                "ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "currency": "USD",
                "balance": "1250.750",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerAccountBalance.model_json_schema().get("example", {})
    ledger_account_balance_instance = LedgerAccountBalance(**example_dict)
    print("----begin example: ledger-account-balance----")
    print(ledger_account_balance_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-account-balance----")
    print(json.dumps(ledger_account_balance_instance.to_minimal_dict(), indent=2))

    print("----end: ledger-account-balance----")