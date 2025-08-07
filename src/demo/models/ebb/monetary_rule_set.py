from __future__ import annotations

import datetime
import json
from typing import Optional, Literal

from pydantic import BaseModel, Field


class MinimalMonetaryRuleSetMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'rule_status',
        'short_desc',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class MonetaryRuleSet(BaseModel, MinimalMonetaryRuleSetMixin):
    """
    Pydantic V2 model for the `monetary_rule_set` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the monetary rule set.")
    rule_status: Literal["SETUP", "ACTIVE", "DEPRECATED", "DELETED"] = Field(
        default="SETUP",
        description="Status of the rule set."
    )
    short_desc: str = Field(..., max_length=40, description="Short description of the rule set.")
    full_desc: Optional[str] = Field(default=None, max_length=255, description="Full description of the rule set.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
    )
    audit_id: Optional[str] = Field(default=None, max_length=26, description="Audit identifier.")

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
                "rule_status": "ACTIVE",
                "short_desc": "Volume Discount Rules",
                "full_desc": "Tiered discount rules based on usage volume for enterprise customers",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = MonetaryRuleSet.model_json_schema().get("example", {})
    monetary_rule_set_instance = MonetaryRuleSet(**example_dict)
    print("----begin example: monetary-rule-set----")
    print(monetary_rule_set_instance.model_dump_json(indent=2))
    print("----begin minmal example: monetary-rule-set----")
    print(json.dumps(monetary_rule_set_instance.to_minimal_dict(), indent=2))
    print("----end: monetary-rule-set----")