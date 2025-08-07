from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalLookMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'namespace',
        'hash',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class Look(BaseModel, MinimalLookMixin):
    """
    Pydantic V2 model for the `look` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=32, description="Unique identifier for the look.")
    hash: str = Field(..., max_length=64, description="Hash value for the look.")
    namespace: str = Field(..., max_length=32, description="Namespace for the look.")
    metadata: Optional[str] = Field(default=None, max_length=1024, description="Metadata for the look.")
    processed_timestamp: Optional[datetime.datetime] = Field(default=None, description="Timestamp when the look was processed.")
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
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGHJKLMNP",
                "hash": "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456",
                "namespace": "billing_data",
                "metadata": '{"source": "merchant_api", "version": "1.0"}',
                "processed_timestamp": "2023-10-27T10:30:00.123456",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = Look.model_json_schema().get("example", {})
    look_instance = Look(**example_dict)
    print("----begin example: look----")
    print(look_instance.model_dump_json(indent=2))
    print("----begin minmal example: look----")
    print(json.dumps(look_instance.to_minimal_dict(), indent=2))
    print("----end: look----")