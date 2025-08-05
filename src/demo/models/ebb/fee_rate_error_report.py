from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ApplyType(str, Enum):
    DEFAULT = "DEFAULT"
    PER_ITEM = "PER_ITEM"
    PERCENTAGE = "PERCENTAGE"
    BOTH = "BOTH"
    NONE = "NONE"
    FLAT = "FLAT"


class MinimalFeeRateErrorReportMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
        'currency',
        'apply_type',
        'resolved_status',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeRateErrorReport(BaseModel, MinimalFeeRateErrorReportMixin):
    """
    Pydantic V2 model for the `fee_rate_error_report` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the fee rate error report.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    currency: str = Field(..., max_length=3, description="Currency for the rate.")
    apply_type: Optional[ApplyType] = Field(default=None, description="How the rate is applied, can be null.")
    resolved_status: Optional[int] = Field(default=0, description="Whether the error has been resolved (0/1).")
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
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "currency": "USD",
                "apply_type": "PER_ITEM",
                "resolved_status": 0,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeRateErrorReport.model_json_schema().get("example", {})
    fee_rate_error_report_instance = FeeRateErrorReport(**example_dict)
    print("----begin example: fee-rate-error-report----")
    print(fee_rate_error_report_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-rate-error-report----")
    print(json.dumps(fee_rate_error_report_instance.to_minimal_dict(), indent=2))

    print("----end: fee-rate-error-report----")