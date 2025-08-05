from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalLedgerAccountKeyMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'ledger_account_key',
        'ledger_account_type',
        'short_desc',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerAccountKey(BaseModel, MinimalLedgerAccountKeyMixin):
    """
    Pydantic V2 model for the `ledger_account_key` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    ledger_account_key: str = Field(..., max_length=32)
    ledger_account_type: str = Field(..., max_length=20)  # ENUM: ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE
    default_gl_code: Optional[str] = Field(default=None, max_length=40)
    short_desc: str = Field(..., max_length=40)
    full_desc: Optional[str] = Field(default=None, max_length=255)
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
                "ledger_account_key": "REVENUE_SUBSCRIPTION_MONTHLY",
                "ledger_account_type": "REVENUE",
                "default_gl_code": "4001-001",
                "short_desc": "Monthly Subscription Revenue",
                "full_desc": "Revenue from monthly subscription fees charged to customers",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerAccountKey.model_json_schema().get("example", {})
    ledger_account_key_instance = LedgerAccountKey(**example_dict)
    print("----begin example: ledger-account-key----")
    print(ledger_account_key_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-account-key----")
    print(json.dumps(ledger_account_key_instance.to_minimal_dict(), indent=2))

    print("----end: ledger-account-key----")