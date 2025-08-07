from __future__ import annotations

import datetime
import json
from typing import Optional, Literal

from pydantic import BaseModel, Field


class MinimalTieredRuleMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'rule_status',
        'rule_alias',
        'tiered_basis',
        'tiered_model',
        'target_entity_type',
        'short_desc',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class TieredRule(BaseModel, MinimalTieredRuleMixin):
    """
    Pydantic V2 model for the `tiered_rule` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the tiered rule.")
    rule_status: Literal["SETUP", "ACTIVE", "DEPRECATED", "DELETED"] = Field(
        default="SETUP",
        description="Status of the rule."
    )
    rule_alias: Optional[str] = Field(default=None, max_length=25, description="Alias for the rule.")
    tiered_basis: Literal["QUANTITY", "VOLUME", "BOTH"] = Field(..., description="Basis for tiered calculation.")
    tiered_model: Literal["APPLY_TO_TIER", "APPLY_TO_ALL"] = Field(..., description="Model for applying tiers.")
    target_entity_type: Literal["MERCHANT", "RESELLER", "DEVELOPER"] = Field(..., description="Target entity type.")
    short_desc: str = Field(..., max_length=40, description="Short description of the rule.")
    full_desc: Optional[str] = Field(default=None, max_length=255, description="Full description of the rule.")
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
                "rule_alias": "VOLUME_DISCOUNT",
                "tiered_basis": "VOLUME",
                "tiered_model": "APPLY_TO_TIER",
                "target_entity_type": "MERCHANT",
                "short_desc": "Volume Based Discount Tiers",
                "full_desc": "Tiered discount structure based on transaction volume for merchants",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = TieredRule.model_json_schema().get("example", {})
    tiered_rule_instance = TieredRule(**example_dict)
    print("----begin example: tiered-rule----")
    print(tiered_rule_instance.model_dump_json(indent=2))
    print("----begin minmal example: tiered-rule----")
    print(json.dumps(tiered_rule_instance.to_minimal_dict(), indent=2))
    print("----end: tiered-rule----")