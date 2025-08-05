from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalLedgerAccountKeyPurposeMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'purpose',
        'ledger_account_key',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerAccountKeyPurpose(BaseModel, MinimalLedgerAccountKeyPurposeMixin):
    """
    Pydantic V2 model for the `ledger_account_key_purpose` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    purpose: str = Field(..., max_length=25)
    ledger_account_key: str = Field(..., max_length=32)
    created_timestamp: datetime.datetime
    audit_id: Optional[str] = Field(default=None, max_length=26)

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
                "purpose": "SUBSCRIPTION_BILLING",
                "ledger_account_key": "REVENUE_SUBSCRIPTION_MONTHLY",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGX",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerAccountKeyPurpose.model_json_schema().get("example", {})
    ledger_account_key_purpose_instance = LedgerAccountKeyPurpose(**example_dict)
    print("----begin example: ledger-account-key-purpose----")
    print(ledger_account_key_purpose_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-account-key-purpose----")
    print(json.dumps(ledger_account_key_purpose_instance.to_minimal_dict(), indent=2))

    print("----end: ledger-account-key-purpose----")