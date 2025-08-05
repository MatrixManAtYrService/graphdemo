from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalLedgerAccountMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'ledger_account_key',
        'gl_code',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerAccount(BaseModel, MinimalLedgerAccountMixin):
    """
    Pydantic V2 model for the `ledger_account` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    ledger_account_key: str = Field(..., max_length=32)
    billing_entity_uuid: str = Field(..., max_length=26)
    gl_code: Optional[str] = Field(default=None, max_length=40)
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
                "ledger_account_key": "REVENUE_RECURRING",
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "gl_code": "4000-001",
                "created_timestamp": "2023-10-27T10:00:00.123456", 
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerAccount.model_json_schema().get("example", {})
    ledger_account_instance = LedgerAccount(**example_dict)
    print("----begin example: ledger-account----")
    print(ledger_account_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-account----")
    print(json.dumps(ledger_account_instance.to_minimal_dict(), indent=2))
    print("----end: ledger-account----")