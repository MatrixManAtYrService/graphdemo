from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalFeeCodeMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
        'short_desc',
        'sort_order',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeCode(BaseModel, MinimalFeeCodeMixin):
    """
    Pydantic V2 model for the `fee_code` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the fee code.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    short_desc: str = Field(..., max_length=40, description="Short description of the fee.")
    full_desc: Optional[str] = Field(default=None, max_length=255, description="Full description of the fee, can be null.")
    sort_order: int = Field(..., description="Sort order for display purposes.")
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
                "fee_category": "RECURRING",
                "fee_code": "MONTHLY_FEE",
                "short_desc": "Monthly subscription fee",
                "full_desc": "Standard monthly subscription fee for basic service plan",
                "sort_order": 10,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeCode.model_json_schema().get("example", {})
    fee_code_instance = FeeCode(**example_dict)
    print("----begin example: fee-code----")
    print(fee_code_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-code----")
    print(json.dumps(fee_code_instance.to_minimal_dict(), indent=2))

    print("----end: fee-code----")