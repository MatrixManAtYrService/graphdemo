from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalLexiAttributeMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'word',
        'lexicon',
        'attr_name',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LexiAttribute(BaseModel, MinimalLexiAttributeMixin):
    """
    Pydantic V2 model for the `lexi_attribute` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=36, description="Unique identifier for the lexi attribute.")
    word: str = Field(..., max_length=512, description="The word or term.")
    lexicon: str = Field(..., max_length=128, description="The lexicon category.")
    attr_name: str = Field(..., max_length=128, description="The attribute name.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    deleted_timestamp: Optional[datetime.datetime] = Field(default=None, description="Timestamp when the record was deleted.")

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                "id": 1,
                "uuid": "01H8X7Y7-Z7QW-ERTY-UIOP-ASDFGHJKLZXC",
                "word": "premium_plan",
                "lexicon": "billing_terms",
                "attr_name": "plan_type",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "deleted_timestamp": None,
            }
        }

if __name__ == "__main__":
    example_dict = LexiAttribute.model_json_schema().get("example", {})
    lexi_attribute_instance = LexiAttribute(**example_dict)
    print("----begin example: lexi-attribute----")
    print(lexi_attribute_instance.model_dump_json(indent=2))
    print("----begin minmal example: lexi-attribute----")
    print(json.dumps(lexi_attribute_instance.to_minimal_dict(), indent=2))
    print("----end: lexi-attribute----")