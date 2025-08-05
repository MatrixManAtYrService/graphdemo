from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalFeeCodeAppMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category',
        'fee_code',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeCodeApp(BaseModel, MinimalFeeCodeAppMixin):
    """
    Pydantic V2 model for the `fee_code_app` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the fee code app.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    developer_uuid: str = Field(..., max_length=13, description="UUID of the developer.")
    developer_app_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the developer app, can be null.")
    app_subscription_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the app subscription, can be null.")
    app_metered_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the app metered resource, can be null.")
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
                "fee_category": "RECURRING",
                "fee_code": "APP_SUBSCRIPTION",
                "developer_uuid": "01H8X7Y7Z7QWE",
                "developer_app_uuid": "01H8X7Y7Z7QWR",
                "app_subscription_uuid": "01H8X7Y7Z7QWT",
                "app_metered_uuid": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeCodeApp.model_json_schema().get("example", {})
    fee_code_app_instance = FeeCodeApp(**example_dict)
    print("----begin example: fee-code-app----")
    print(fee_code_app_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-code-app----")
    print(json.dumps(fee_code_app_instance.to_minimal_dict(), indent=2))

    print("----end: fee-code-app----")