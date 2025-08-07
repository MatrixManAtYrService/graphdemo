from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalModelFeeSummaryMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
        'currency',
        'total_period_units',
        'total_basis_amount',
        'total_fee_amount',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class ModelFeeSummary(BaseModel, MinimalModelFeeSummaryMixin):
    """
    Pydantic V2 model for the `model_fee_summary` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the model fee summary.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    billing_date: datetime.date = Field(..., description="The billing date for this summary.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    currency: str = Field(..., max_length=3, description="Currency code (e.g., USD).")
    total_period_units: Decimal = Field(
        default=Decimal("0.0000"),
        max_digits=12,
        decimal_places=4,
        description="Total units for the period."
    )
    total_basis_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Total basis amount for calculation."
    )
    total_fee_amount: Decimal = Field(
        default=Decimal("0.000"),
        max_digits=12,
        decimal_places=3,
        description="Total fee amount calculated."
    )
    fee_rate_uuid: str = Field(..., max_length=26, description="UUID of the fee rate.")
    request_uuid: str = Field(..., max_length=26, description="UUID of the request.")
    invoice_info_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the invoice info.")
    fee_code_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of fee code ledger account.")
    credit_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of credit ledger account.")
    debit_ledger_account_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of debit ledger account.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "billing_date": "2023-11-01",
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "currency": "USD",
                "total_period_units": "1.0000",
                "total_basis_amount": "99.990",
                "total_fee_amount": "99.990",
                "fee_rate_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGB",
                "invoice_info_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGC",
                "fee_code_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGD",
                "credit_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGE",
                "debit_ledger_account_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGF",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = ModelFeeSummary.model_json_schema().get("example", {})
    model_fee_summary_instance = ModelFeeSummary(**example_dict)
    print("----begin example: model-fee-summary----")
    print(model_fee_summary_instance.model_dump_json(indent=2))
    print("----begin minmal example: model-fee-summary----")
    print(json.dumps(model_fee_summary_instance.to_minimal_dict(), indent=2))
    print("----end: model-fee-summary----")