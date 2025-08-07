from __future__ import annotations

import datetime
import json

from pydantic import BaseModel, Field


class MinimalLookDataMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'payload',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LookData(BaseModel, MinimalLookDataMixin):
    """
    Pydantic V2 model for the `look_data` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    look_uuid: str = Field(..., max_length=32, description="UUID of the associated look.")
    payload: bytes = Field(..., description="Binary payload data.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
            bytes: lambda v: v.decode('utf-8', errors='replace'),
        }
        json_schema_extra = {
            "example": {
                "id": 1,
                "look_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGHJKLMNP",
                "payload": b'{"billing_cycle": "monthly", "fee_structure": "tiered"}',
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = LookData.model_json_schema().get("example", {})
    look_data_instance = LookData(**example_dict)
    print("----begin example: look-data----")
    print(look_data_instance.model_dump_json(indent=2))
    print("----begin minmal example: look-data----")
    print(json.dumps(look_data_instance.to_minimal_dict(), indent=2))
    print("----end: look-data----")