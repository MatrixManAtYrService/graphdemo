from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalMiscSpecifierMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'misc_specifier',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class MiscSpecifier(BaseModel, MinimalMiscSpecifierMixin):
    """
    Pydantic V2 model for the `misc_specifier` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the misc specifier.")
    misc_specifier: str = Field(..., max_length=25, description="Miscellaneous specifier value.")
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
                "misc_specifier": "CUSTOM_FEE_TYPE",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = MiscSpecifier.model_json_schema().get("example", {})
    misc_specifier_instance = MiscSpecifier(**example_dict)
    print("----begin example: misc-specifier----")
    print(misc_specifier_instance.model_dump_json(indent=2))
    print("----begin minmal example: misc-specifier----")
    print(json.dumps(misc_specifier_instance.to_minimal_dict(), indent=2))
    print("----end: misc-specifier----")