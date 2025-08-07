from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalPlanActionErrorMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'error_code',
        'posting_attempts',
        'resolved',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class PlanActionError(BaseModel, MinimalPlanActionErrorMixin):
    """
    Pydantic V2 model for the `plan_action_error` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the plan action error.")
    plan_action_uuid: str = Field(..., max_length=26, description="UUID of the plan action.")
    request_uuid: str = Field(..., max_length=26, description="UUID of the request.")
    posting_date: datetime.date = Field(..., description="Date for posting.")
    original_request_uuid: str = Field(..., max_length=26, description="UUID of the original request.")
    original_posting_date: datetime.date = Field(..., description="Original posting date.")
    posting_attempts: int = Field(default=1, description="Number of posting attempts.")
    error_code: str = Field(..., max_length=25, description="Error code.")
    error_details: Optional[str] = Field(default=None, description="Detailed error information.")
    resolved: int = Field(default=0, description="Whether the error has been resolved (0/1).")
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
                "plan_action_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "posting_date": "2023-11-01",
                "original_request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGB",
                "original_posting_date": "2023-10-31",
                "posting_attempts": 3,
                "error_code": "RATE_NOT_FOUND",
                "error_details": "Fee rate configuration missing for merchant plan",
                "resolved": 0,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T12:30:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = PlanActionError.model_json_schema().get("example", {})
    plan_action_error_instance = PlanActionError(**example_dict)
    print("----begin example: plan-action-error----")
    print(plan_action_error_instance.model_dump_json(indent=2))
    print("----begin minmal example: plan-action-error----")
    print(json.dumps(plan_action_error_instance.to_minimal_dict(), indent=2))
    print("----end: plan-action-error----")