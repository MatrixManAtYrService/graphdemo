from __future__ import annotations

import datetime
import json
from typing import Literal

from pydantic import BaseModel, Field


class MinimalMonetaryRuleAliasMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'rule_alias',
        'rule_type',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class MonetaryRuleAlias(BaseModel, MinimalMonetaryRuleAliasMixin):
    """
    Pydantic V2 model for the `monetary_rule_alias` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the monetary rule alias.")
    rule_alias: str = Field(..., max_length=25, description="Alias name for the rule.")
    rule_type: Literal["AUTO_ADJUST", "TIERED"] = Field(..., description="Type of rule.")
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
                "rule_alias": "VOLUME_DISCOUNT",
                "rule_type": "TIERED",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = MonetaryRuleAlias.model_json_schema().get("example", {})
    monetary_rule_alias_instance = MonetaryRuleAlias(**example_dict)
    print("----begin example: monetary-rule-alias----")
    print(monetary_rule_alias_instance.model_dump_json(indent=2))
    print("----begin minmal example: monetary-rule-alias----")
    print(json.dumps(monetary_rule_alias_instance.to_minimal_dict(), indent=2))
    print("----end: monetary-rule-alias----")