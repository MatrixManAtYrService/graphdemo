from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class BillingEntityUuidSource(str, Enum):
    TRANSACTION = "TRANSACTION"
    CLOVER = "CLOVER"
    ROLLUP_1 = "ROLLUP_1"
    ROLLUP_2 = "ROLLUP_2"
    ROLLUP_3 = "ROLLUP_3"


class MinimalFeeCodeLedgerAccountMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
        'effective_date',
        'credit_ledger_account_key',
        'debit_ledger_account_key',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeCodeLedgerAccount(BaseModel, MinimalFeeCodeLedgerAccountMixin):
    """
    Pydantic V2 model for the `fee_code_ledger_account` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the fee code ledger account.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: Optional[str] = Field(default=None, max_length=25, description="Code of the fee, can be null.")
    effective_date: datetime.date = Field(..., description="Date when the ledger account mapping becomes effective.")
    credit_ledger_account_key: str = Field(..., max_length=32, description="Key for the credit ledger account.")
    credit_billing_entity_uuid_source: BillingEntityUuidSource = Field(..., description="Source for credit billing entity UUID.")
    debit_ledger_account_key: str = Field(..., max_length=32, description="Key for the debit ledger account.")
    debit_billing_entity_uuid_source: BillingEntityUuidSource = Field(..., description="Source for debit billing entity UUID.")
    deleted_date: Optional[datetime.date] = Field(default=None, description="Date when the mapping was deleted, can be null.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
    )
    audit_id: Optional[str] = Field(default=None, max_length=26, description="Audit identifier, can be null.")

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
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "effective_date": "2023-10-01",
                "credit_ledger_account_key": "REVENUE_MONTHLY_FEES",
                "credit_billing_entity_uuid_source": "TRANSACTION",
                "debit_ledger_account_key": "AR_CUSTOMER_RECEIVABLES",
                "debit_billing_entity_uuid_source": "CLOVER",
                "deleted_date": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = FeeCodeLedgerAccount.model_json_schema().get("example", {})
    fee_code_ledger_account_instance = FeeCodeLedgerAccount(**example_dict)
    print("----begin example: fee-code-ledger-account----")
    print(fee_code_ledger_account_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-code-ledger-account----")
    print(json.dumps(fee_code_ledger_account_instance.to_minimal_dict(), indent=2))

    print("----end: fee-code-ledger-account----")