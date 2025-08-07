from __future__ import annotations

import datetime
import json
from typing import Optional, Literal

from pydantic import BaseModel, Field


class MinimalLexiRuleMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'lexicon',
        'rule_name',
        'rule_type',
        'priority',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LexiRule(BaseModel, MinimalLexiRuleMixin):
    """
    Pydantic V2 model for the `lexi_rule` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=36, description="Unique identifier for the lexi rule.")
    parent_uuid: Optional[str] = Field(default=None, max_length=36, description="UUID of the parent rule.")
    lexicon: str = Field(..., max_length=128, description="The lexicon category.")
    rule_name: str = Field(..., max_length=128, description="Name of the rule.")
    description: Optional[str] = Field(default=None, max_length=512, description="Description of the rule.")
    rule_condition: Optional[str] = Field(default=None, max_length=512, description="Condition for the rule.")
    target_attributes: Optional[str] = Field(default=None, max_length=512, description="Target attributes for the rule.")
    priority: int = Field(default=1, description="Priority of the rule.")
    rule_type: Literal["SIMPLE", "UNIT", "ACTIVATION", "CONDITIONAL"] = Field(..., description="Type of rule.")
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
                "parent_uuid": None,
                "lexicon": "billing_terms",
                "rule_name": "premium_discount",
                "description": "Apply discount for premium customers",
                "rule_condition": "plan_type == 'premium'",
                "target_attributes": "discount_rate",
                "priority": 10,
                "rule_type": "CONDITIONAL",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "deleted_timestamp": None,
            }
        }

if __name__ == "__main__":
    example_dict = LexiRule.model_json_schema().get("example", {})
    lexi_rule_instance = LexiRule(**example_dict)
    print("----begin example: lexi-rule----")
    print(lexi_rule_instance.model_dump_json(indent=2))
    print("----begin minmal example: lexi-rule----")
    print(json.dumps(lexi_rule_instance.to_minimal_dict(), indent=2))
    print("----end: lexi-rule----")