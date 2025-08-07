from __future__ import annotations

import datetime
import json

from pydantic import BaseModel, Field


class MinimalSkipFeeCategoryLexiTagMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class SkipFeeCategoryLexiTag(BaseModel, MinimalSkipFeeCategoryLexiTagMixin):
    """
    Pydantic V2 model for the `skip_fee_category_lexi_tag` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the skip fee category lexi tag.")
    fee_category: str = Field(..., max_length=25, description="Fee category to skip in lexi processing.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
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
                "fee_category": "INTERNAL_FEE",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = SkipFeeCategoryLexiTag.model_json_schema().get("example", {})
    skip_fee_category_lexi_tag_instance = SkipFeeCategoryLexiTag(**example_dict)
    print("----begin example: skip-fee-category-lexi-tag----")
    print(skip_fee_category_lexi_tag_instance.model_dump_json(indent=2))
    print("----begin minmal example: skip-fee-category-lexi-tag----")
    print(json.dumps(skip_fee_category_lexi_tag_instance.to_minimal_dict(), indent=2))
    print("----end: skip-fee-category-lexi-tag----")