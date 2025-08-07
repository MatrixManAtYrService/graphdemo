from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional, Literal

from pydantic import BaseModel, Field


class MinimalLedgerJournalMutationMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'mutation_action',
        'cr_db',
        'currency',
        'amount',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerJournalMutation(BaseModel, MinimalLedgerJournalMutationMixin):
    """
    Pydantic V2 model for the `ledger_journal_mutation` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    mutation_action: Literal["UPDATE", "DELETE"] = Field(..., description="Type of mutation action.")
    mutation_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the mutation occurred."
    )
    ledger_journal_id: int = Field(..., description="ID of the ledger journal record.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the ledger journal.")
    ledger_account_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the ledger account.")
    journal_date: Optional[datetime.date] = Field(default=None, description="Journal entry date.")
    ref_uuid_type: Optional[Literal["FEE_SUMMARY", "SETTLE_EXPORT", "SETTLE_IMPORT", "FEE_TAX"]] = Field(
        default=None, description="Type of reference UUID."
    )
    ref_uuid: Optional[str] = Field(default=None, max_length=26, description="Reference UUID.")
    cr_db: Optional[Literal["CREDIT", "DEBIT"]] = Field(default=None, description="Credit or debit indicator.")
    currency: Optional[str] = Field(default=None, max_length=3, description="Currency code.")
    amount: Optional[Decimal] = Field(
        default=None,
        max_digits=12,
        decimal_places=3,
        description="Transaction amount."
    )
    created_timestamp: Optional[datetime.datetime] = Field(default=None, description="Timestamp when the original record was created.")

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
                "ledger_journal_id": 123,
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "journal_date": "2023-11-01",
                "ref_uuid_type": "FEE_SUMMARY",
                "ref_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "cr_db": "DEBIT",
                "currency": "USD",
                "amount": "99.990",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerJournalMutation.model_json_schema().get("example", {})
    ledger_journal_mutation_instance = LedgerJournalMutation(**example_dict)
    print("----begin example: ledger-journal-mutation----")
    print(ledger_journal_mutation_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-journal-mutation----")
    print(json.dumps(ledger_journal_mutation_instance.to_minimal_dict(), indent=2))
    print("----end: ledger-journal-mutation----")