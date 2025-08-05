from __future__ import annotations

import datetime
import json

from pydantic import BaseModel, Field


class MinimalFeeCategoryMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'sort_order',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeCategory(BaseModel, MinimalFeeCategoryMixin):
    """
    Pydantic V2 model for the `fee_category` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the fee category.")
    fee_category: str = Field(..., max_length=25, description="Name of the fee category.")
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
                "sort_order": 10,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeCategory.model_json_schema().get("example", {})
    fee_category_instance = FeeCategory(**example_dict)
    print("----begin example: fee-category----")
    print(fee_category_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-category----")
    print(json.dumps(fee_category_instance.to_minimal_dict(), indent=2))

    print("----end: fee-category----")