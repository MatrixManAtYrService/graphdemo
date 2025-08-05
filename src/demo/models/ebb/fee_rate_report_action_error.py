from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalFeeRateReportActionErrorMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'action_type',
        'created_timestamp',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FeeRateReportActionError(BaseModel, MinimalFeeRateReportActionErrorMixin):
    """
    Pydantic V2 model for the `fee_rate_report_action_error` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    billing_entity_uuid: str = Field(..., max_length=26)
    fee_rate_error_report_uuid: str = Field(..., max_length=26)
    action_error_uuid: str = Field(..., max_length=26)
    action_type: str = Field(..., max_length=25)
    created_timestamp: datetime.datetime

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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "fee_rate_error_report_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGY",
                "action_error_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "action_type": "PLAN_ACTION",
                "created_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = FeeRateReportActionError.model_json_schema().get("example", {})
    fee_rate_report_action_error_instance = FeeRateReportActionError(**example_dict)
    print("----begin example: fee-rate-report-action-error----")
    print(fee_rate_report_action_error_instance.model_dump_json(indent=2))
    print("----begin minmal example: fee-rate-report-action-error----")
    print(json.dumps(fee_rate_report_action_error_instance.to_minimal_dict(), indent=2))

    print("----end: fee-rate-report-action-error----")