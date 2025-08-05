from __future__ import annotations

import datetime
import json

from pydantic import BaseModel, Field


class MinimalLedgerAccountActionMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'action',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerAccountAction(BaseModel, MinimalLedgerAccountActionMixin):
    """
    Pydantic V2 model for the `ledger_account_action` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    action: str = Field(..., max_length=25)
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
                "action": "DEBIT",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerAccountAction.model_json_schema().get("example", {})
    ledger_account_action_instance = LedgerAccountAction(**example_dict)
    print("----begin example: ledger-account-action----")
    print(ledger_account_action_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-account-action----")
    print(json.dumps(ledger_account_action_instance.to_minimal_dict(), indent=2))

    print("----end: ledger-account-action----")