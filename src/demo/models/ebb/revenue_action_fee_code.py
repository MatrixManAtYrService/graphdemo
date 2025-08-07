from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalRevenueActionFeeCodeMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'fee_category_group',
        'revenue_group',
        'revenue_action_type',
        'fee_category',
        'fee_code',
        'effective_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class RevenueActionFeeCode(BaseModel, MinimalRevenueActionFeeCodeMixin):
    """
    Pydantic V2 model for the `revenue_action_fee_code` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the revenue action fee code.")
    fee_category_group: str = Field(..., max_length=25, description="Fee category group.")
    revenue_group: Optional[str] = Field(default=None, max_length=25, description="Revenue group.")
    revenue_share_group: Optional[str] = Field(default=None, max_length=20, description="Revenue share group.")
    developer_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the developer.")
    developer_app_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the developer app.")
    app_subscription_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the app subscription.")
    app_metered_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the app metered.")
    merchant_plan_uuid: Optional[str] = Field(default=None, max_length=13, description="UUID of the merchant plan.")
    revenue_action_type: str = Field(..., max_length=25, description="Type of revenue action.")
    effective_date: datetime.date = Field(..., description="Date when the fee code becomes effective.")
    fee_category: str = Field(..., max_length=25, description="Category of the fee.")
    fee_code: str = Field(..., max_length=25, description="Code of the fee.")
    deleted_date: Optional[datetime.date] = Field(default=None, description="Date when the fee code was deleted.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
    )
    audit_id: Optional[str] = Field(default=None, max_length=26, description="Audit identifier.")

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
                "fee_category_group": "APP_REVENUE",
                "revenue_group": "SUBSCRIPTION",
                "revenue_share_group": "STANDARD",
                "developer_uuid": "01H8X7Y7Z7QWE",
                "developer_app_uuid": "01H8X7Y7Z7QWE",
                "app_subscription_uuid": "01H8X7Y7Z7QWE",
                "app_metered_uuid": None,
                "merchant_plan_uuid": None,
                "revenue_action_type": "REVENUE_SHARE",
                "effective_date": "2023-11-01",
                "fee_category": "REVENUE",
                "fee_code": "APP_SHARE",
                "deleted_date": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = RevenueActionFeeCode.model_json_schema().get("example", {})
    revenue_action_fee_code_instance = RevenueActionFeeCode(**example_dict)
    print("----begin example: revenue-action-fee-code----")
    print(revenue_action_fee_code_instance.model_dump_json(indent=2))
    print("----begin minmal example: revenue-action-fee-code----")
    print(json.dumps(revenue_action_fee_code_instance.to_minimal_dict(), indent=2))
    print("----end: revenue-action-fee-code----")