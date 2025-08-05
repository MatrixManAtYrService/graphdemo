from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class RuleStatus(str, Enum):
    SETUP = "SETUP"
    ACTIVE = "ACTIVE"
    DEPRECATED = "DEPRECATED"
    DELETED = "DELETED"


class TargetEntityType(str, Enum):
    MERCHANT = "MERCHANT"
    RESELLER = "RESELLER"
    DEVELOPER = "DEVELOPER"


class MinimalAutoAdjustRuleMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'rule_status',
        'rate_fee_category',
        'rate_fee_code',
        'target_entity_type',
        'short_desc',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class AutoAdjustRule(BaseModel, MinimalAutoAdjustRuleMixin):
    """
    Pydantic V2 model for the `auto_adjust_rule` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the auto adjust rule.")
    rule_status: RuleStatus = Field(default=RuleStatus.SETUP, description="Status of the rule.")
    rule_alias: Optional[str] = Field(default=None, max_length=25, description="Alias for the rule, can be null.")
    rate_fee_category: str = Field(..., max_length=25, description="Fee category for the rate.")
    rate_fee_code: str = Field(..., max_length=25, description="Fee code for the rate.")
    target_entity_type: TargetEntityType = Field(..., description="Type of target entity.")
    short_desc: str = Field(..., max_length=40, description="Short description of the rule.")
    full_desc: Optional[str] = Field(default=None, max_length=255, description="Full description of the rule, can be null.")
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
                "rule_status": "ACTIVE",
                "rule_alias": "VOLUME_DISCOUNT",
                "rate_fee_category": "RECURRING",
                "rate_fee_code": "MONTHLY_FEE",
                "target_entity_type": "MERCHANT",
                "short_desc": "Volume-based discount rule",
                "full_desc": "Provides automatic adjustments based on monthly transaction volume thresholds",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = AutoAdjustRule.model_json_schema().get("example", {})
    auto_adjust_rule_instance = AutoAdjustRule(**example_dict)
    print("----begin example: auto-adjust-rule----")
    print(auto_adjust_rule_instance.model_dump_json(indent=2))
    print("----begin minmal example: auto-adjust-rule----")
    print(json.dumps(auto_adjust_rule_instance.to_minimal_dict(), indent=2))

    print("----end: auto-adjust-rule----")