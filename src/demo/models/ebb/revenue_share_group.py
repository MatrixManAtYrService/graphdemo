from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalRevenueShareGroupMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'revenue_share_group',
        'short_desc',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class RevenueShareGroup(BaseModel, MinimalRevenueShareGroupMixin):
    """
    Pydantic V2 model for the `revenue_share_group` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the revenue share group.")
    revenue_share_group: str = Field(..., max_length=20, description="Revenue share group name.")
    short_desc: Optional[str] = Field(default=None, max_length=40, description="Short description.")
    description: Optional[str] = Field(default=None, max_length=255, description="Full description.")
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
                "revenue_share_group": "STANDARD_30",
                "short_desc": "Standard 30% Revenue Share",
                "description": "Standard revenue sharing arrangement with 30% developer share",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = RevenueShareGroup.model_json_schema().get("example", {})
    revenue_share_group_instance = RevenueShareGroup(**example_dict)
    print("----begin example: revenue-share-group----")
    print(revenue_share_group_instance.model_dump_json(indent=2))
    print("----begin minmal example: revenue-share-group----")
    print(json.dumps(revenue_share_group_instance.to_minimal_dict(), indent=2))
    print("----end: revenue-share-group----")