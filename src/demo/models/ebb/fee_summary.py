from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalFeeSummaryMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'total_period_units',
        'total_fee_amount',
        'total_basis_amount',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeSummary(BaseModel, MinimalFeeSummaryMixin):
    """
    Pydantic V2 model for the `fee_summary` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    billing_entity_uuid: str = Field(..., max_length=26)
    billing_date: datetime.date
    fee_category: str = Field(..., max_length=25)
    fee_code: str = Field(..., max_length=25)
    currency: str = Field(..., max_length=3)
    total_period_units: Decimal = Field(..., max_digits=12, decimal_places=4)
    abs_period_units: Decimal = Field(..., max_digits=12, decimal_places=4)
    total_basis_amount: Decimal = Field(..., max_digits=12, decimal_places=3)
    abs_basis_amount: Decimal = Field(..., max_digits=12, decimal_places=3)
    total_fee_amount: Decimal = Field(..., max_digits=12, decimal_places=3)
    fee_rate_uuid: str = Field(..., max_length=26)
    request_uuid: str = Field(..., max_length=26)
    invoice_info_uuid: Optional[str] = Field(default=None, max_length=26)
    fee_code_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26)
    credit_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26)
    debit_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26)
    exclude_from_invoice: int
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "billing_date": "2023-10-27",
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "currency": "USD",
                "total_period_units": "1.0000",
                "abs_period_units": "1.0000",
                "total_basis_amount": "29.990",
                "abs_basis_amount": "29.990",
                "total_fee_amount": "29.990",
                "fee_rate_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGY",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "invoice_info_uuid": "01H8X7Y7Z7QWERTYUIOPASDFG1",
                "fee_code_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFG2",
                "credit_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFG3",
                "debit_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFG4",
                "exclude_from_invoice": 0,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeSummary.model_json_schema().get("example", {})
    fee_summary_instance = FeeSummary(**example_dict)
    print("----begin example: fee-summary----")
    print(fee_summary_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-summary----")
    print(json.dumps(fee_summary_instance.to_minimal_dict(), indent=2))

    print("----end: fee-summary----")
