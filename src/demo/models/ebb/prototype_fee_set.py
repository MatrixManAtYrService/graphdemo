from __future__ import annotations

import datetime
import json
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Disposition(str, Enum):
    DRAFT = "DRAFT"
    PROMOTED = "PROMOTED"
    REMOVED = "REMOVED"


class MinimalPrototypeFeeSetMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'name',
        'disposition',
        'effective_date',
        'description',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class PrototypeFeeSet(BaseModel, MinimalPrototypeFeeSetMixin):
    """
    Pydantic V2 model for the `prototype_fee_set` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    name: str = Field(..., max_length=40)
    disposition: Disposition
    description: Optional[str] = Field(default=None, max_length=255)
    effective_date: datetime.date
    disposition_datetime: datetime.datetime
    created_timestamp: datetime.datetime
    modified_timestamp: datetime.datetime

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
                "name": "STANDARD_MONTHLY_FEES",
                "disposition": "PROMOTED",
                "description": "Standard monthly billing fee structure for enterprise customers",
                "effective_date": "2023-10-27",
                "disposition_datetime": "2023-10-27T10:00:00.123456",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = PrototypeFeeSet.model_json_schema().get("example", {})
    prototype_fee_set_instance = PrototypeFeeSet(**example_dict)
    print("----begin example: prototype-fee-set----")
    print(prototype_fee_set_instance.model_dump_json(indent=2))
    print("----begin minmal example: prototype-fee-set----")
    print(json.dumps(prototype_fee_set_instance.to_minimal_dict(), indent=2))
    print("----end: prototype-fee-set----")