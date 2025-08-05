from __future__ import annotations

import datetime
import json

from pydantic import BaseModel, Field


class MinimalDeserializableFailureMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'topic',
        'channel',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class DeserializableFailure(BaseModel, MinimalDeserializableFailureMixin):
    """
    Pydantic V2 model for the `deserializable_failure` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=36, description="Unique identifier for the deserializable failure.")
    topic: str = Field(..., max_length=127, description="Message topic.")
    channel: str = Field(..., max_length=127, description="Communication channel.")
    b64: str = Field(..., description="Base64-encoded failure data.")
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
                "uuid": "01H8X7Y7-Z7QW-ERTY-UIOP-ASDFGHJKLZXC",
                "topic": "billing-events",
                "channel": "cellular-usage",
                "b64": "eyJtZXNzYWdlIjoiZGVzZXJpYWxpemF0aW9uIGZhaWx1cmUifQ==",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = DeserializableFailure.model_json_schema().get("example", {})
    deserializable_failure_instance = DeserializableFailure(**example_dict)
    print("----begin example: deserializable-failure----")
    print(deserializable_failure_instance.model_dump_json(indent=2))
    print("----begin minmal example: deserializable-failure----")
    print(json.dumps(deserializable_failure_instance.to_minimal_dict(), indent=2))

    print("----end: deserializable-failure----")