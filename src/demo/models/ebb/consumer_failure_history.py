from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalConsumerFailureHistoryMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'environment',
        'channel',
        'topic',
        'cause',
        'comment',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class ConsumerFailureHistory(BaseModel, MinimalConsumerFailureHistoryMixin):
    """
    Pydantic V2 model for the `consumer_failure_history` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=36, description="Unique identifier for the consumer failure history.")
    environment: str = Field(..., max_length=25, description="Environment where the failure occurred.")
    reference_id: str = Field(..., max_length=13, description="Reference identifier.")
    payload: str = Field(..., description="Failure payload data.")
    channel: Optional[str] = Field(default=None, max_length=127, description="Communication channel, can be null.")
    topic: Optional[str] = Field(default=None, max_length=127, description="Message topic, can be null.")
    cause: str = Field(..., max_length=100, description="Cause of the failure.")
    message: Optional[str] = Field(default=None, max_length=500, description="Failure message, can be null.")
    comment: Optional[str] = Field(default=None, max_length=500, description="Comment about the failure, can be null.")
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
                "environment": "PRODUCTION",
                "reference_id": "01H8X7Y7Z7QWE",
                "payload": '{"message_id": "12345", "error": "Invalid format"}',
                "channel": "billing-events",
                "topic": "cellular-usage",
                "cause": "VALIDATION_ERROR",
                "message": "Message failed validation due to missing required field",
                "comment": "Moved to history after manual resolution",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = ConsumerFailureHistory.model_json_schema().get("example", {})
    consumer_failure_history_instance = ConsumerFailureHistory(**example_dict)
    print("----begin example: consumer-failure-history----")
    print(consumer_failure_history_instance.model_dump_json(indent=2))
    print("----begin minmal example: consumer-failure-history----")
    print(json.dumps(consumer_failure_history_instance.to_minimal_dict(), indent=2))

    print("----end: consumer-failure-history----")