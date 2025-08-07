from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalProcessingNoteMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'note_code',
        'notes',
        'process_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class ProcessingNote(BaseModel, MinimalProcessingNoteMixin):
    """
    Pydantic V2 model for the `processing_note` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the processing note.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    process_date: Optional[datetime.date] = Field(default=None, description="Date when the processing occurred.")
    note_code: str = Field(..., max_length=25, description="Code for the note type.")
    notes: Optional[str] = Field(default=None, max_length=512, description="Processing notes content.")
    request_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the request.")
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "process_date": "2023-11-01",
                "note_code": "BILLING_CYCLE",
                "notes": "Monthly billing cycle processed successfully with 1,234 transactions",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = ProcessingNote.model_json_schema().get("example", {})
    processing_note_instance = ProcessingNote(**example_dict)
    print("----begin example: processing-note----")
    print(processing_note_instance.model_dump_json(indent=2))
    print("----begin minmal example: processing-note----")
    print(json.dumps(processing_note_instance.to_minimal_dict(), indent=2))
    print("----end: processing-note----")