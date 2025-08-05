from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalBillingHierarchyMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'hierarchy_type',
        'effective_date',
        'deleted_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingHierarchy(BaseModel, MinimalBillingHierarchyMixin):
    """
    Pydantic V2 model for the `billing_hierarchy` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the billing hierarchy.")
    hierarchy_type: str = Field(..., max_length=20, description="Type of hierarchy.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    effective_date: datetime.date = Field(..., description="Date when the hierarchy becomes effective.")
    deleted_date: Optional[datetime.date] = Field(default=None, description="Date when the hierarchy was deleted, can be null.")
    parent_billing_hierarchy_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of parent hierarchy, can be null.")
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "effective_date": "2023-10-01",
                "deleted_date": None,
                "parent_billing_hierarchy_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = BillingHierarchy.model_json_schema().get("example", {})
    billing_hierarchy_instance = BillingHierarchy(**example_dict)
    print("----begin example: billing-hierarchy----")
    print(billing_hierarchy_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-hierarchy----")
    print(json.dumps(billing_hierarchy_instance.to_minimal_dict(), indent=2))

    print("----end: billing-hierarchy----")