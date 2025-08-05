from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalLedgerAccountTransitionMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'action',
        'effective_date',
        'credit_ledger_account_key',
        'debit_ledger_account_key',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerAccountTransition(BaseModel, MinimalLedgerAccountTransitionMixin):
    """
    Pydantic V2 model for the `ledger_account_transition` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    action: str = Field(..., max_length=25)
    effective_date: datetime.date
    lookup_ledger_account_key: str = Field(..., max_length=32)
    credit_ledger_account_key: str = Field(..., max_length=32)
    credit_billing_entity_uuid_source: str = Field(..., max_length=20)  # ENUM: TRANSACTION, CLOVER, ROLLUP_1, ROLLUP_2, ROLLUP_3
    debit_ledger_account_key: str = Field(..., max_length=32)
    debit_billing_entity_uuid_source: str = Field(..., max_length=20)  # ENUM: TRANSACTION, CLOVER, ROLLUP_1, ROLLUP_2, ROLLUP_3
    deleted_date: Optional[datetime.date] = Field(default=None)
    created_timestamp: datetime.datetime
    modified_timestamp: datetime.datetime
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
                "action": "SUBSCRIPTION_CHARGE",
                "effective_date": "2023-10-27",
                "lookup_ledger_account_key": "REVENUE_SUBSCRIPTION_MONTHLY",
                "credit_ledger_account_key": "REVENUE_SUBSCRIPTION_MONTHLY",
                "credit_billing_entity_uuid_source": "TRANSACTION",
                "debit_ledger_account_key": "ACCOUNTS_RECEIVABLE",
                "debit_billing_entity_uuid_source": "CLOVER",
                "deleted_date": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGX",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerAccountTransition.model_json_schema().get("example", {})
    ledger_account_transition_instance = LedgerAccountTransition(**example_dict)
    print("----begin example: ledger-account-transition----")
    print(ledger_account_transition_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-account-transition----")
    print(json.dumps(ledger_account_transition_instance.to_minimal_dict(), indent=2))

    print("----end: ledger-account-transition----")