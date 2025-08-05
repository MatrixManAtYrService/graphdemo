from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalCellularActionFeeCodeMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'carrier',
        'cellular_action_type',
        'fee_category',
        'fee_code',
        'effective_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class CellularActionFeeCode(BaseModel, MinimalCellularActionFeeCodeMixin):
    """
    Pydantic V2 model for the `cellular_action_fee_code` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the cellular action fee code.")
    merchant_plan_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the merchant plan, can be null.")
    carrier: Optional[str] = Field(default=None, max_length=25, description="Cellular carrier name, can be null.")
    cellular_action_type: str = Field(..., max_length=25, description="Type of cellular action.")
    effective_date: datetime.date = Field(..., description="Date when the fee code becomes effective.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    deleted_date: Optional[datetime.date] = Field(default=None, description="Date when the fee code was deleted, can be null.")
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
                "merchant_plan_uuid": "01H8X7Y7Z7QWE",
                "carrier": "VERIZON",
                "cellular_action_type": "DATA_USAGE",
                "effective_date": "2023-10-01",
                "fee_category": "USAGE",
                "fee_code": "DATA_OVERAGE",
                "deleted_date": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = CellularActionFeeCode.model_json_schema().get("example", {})
    cellular_action_fee_code_instance = CellularActionFeeCode(**example_dict)
    print("----begin example: cellular-action-fee-code----")
    print(cellular_action_fee_code_instance.model_dump_json(indent=2))
    print("----begin minmal example: cellular-action-fee-code----")
    print(json.dumps(cellular_action_fee_code_instance.to_minimal_dict(), indent=2))

    print("----end: cellular-action-fee-code----")