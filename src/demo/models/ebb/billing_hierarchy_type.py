from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalBillingHierarchyTypeMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'hierarchy_type',
        'description',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingHierarchyType(BaseModel, MinimalBillingHierarchyTypeMixin):
    """
    Pydantic V2 model for the `billing_hierarchy_type` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the billing hierarchy type.")
    hierarchy_type: str = Field(..., max_length=20, description="Type of hierarchy.")
    description: Optional[str] = Field(default=None, max_length=255, description="Description of the hierarchy type, can be null.")
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
                "hierarchy_type": "STANDARD",
                "description": "Standard billing hierarchy for regular merchants",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = BillingHierarchyType.model_json_schema().get("example", {})
    billing_hierarchy_type_instance = BillingHierarchyType(**example_dict)
    print("----begin example: billing-hierarchy-type----")
    print(billing_hierarchy_type_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-hierarchy-type----")
    print(json.dumps(billing_hierarchy_type_instance.to_minimal_dict(), indent=2))

    print("----end: billing-hierarchy-type----")