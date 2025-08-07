from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalTieredPricingMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'effective_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class TieredPricing(BaseModel, MinimalTieredPricingMixin):
    """
    Pydantic V2 model for the `tiered_pricing` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the tiered pricing.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    tiered_rule_uuid: str = Field(..., max_length=26, description="UUID of the tiered rule.")
    effective_date: datetime.date = Field(..., description="Date when the pricing becomes effective.")
    deleted_date: Optional[datetime.date] = Field(default=None, description="Date when the pricing was deleted.")
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "tiered_rule_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "effective_date": "2023-11-01",
                "deleted_date": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGB",
            }
        }

if __name__ == "__main__":
    example_dict = TieredPricing.model_json_schema().get("example", {})
    tiered_pricing_instance = TieredPricing(**example_dict)
    print("----begin example: tiered-pricing----")
    print(tiered_pricing_instance.model_dump_json(indent=2))
    print("----begin minmal example: tiered-pricing----")
    print(json.dumps(tiered_pricing_instance.to_minimal_dict(), indent=2))
    print("----end: tiered-pricing----")