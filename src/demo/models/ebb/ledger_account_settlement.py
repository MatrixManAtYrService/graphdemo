from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalLedgerAccountSettlementMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'ledger_account_key',
        'effective_date',
        'settlement_item_code',
        'settlement_desc',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class LedgerAccountSettlement(BaseModel, MinimalLedgerAccountSettlementMixin):
    """
    Pydantic V2 model for the `ledger_account_settlement` table.
    """
    id: int = Field(..., gt=0)
    uuid: str = Field(..., max_length=26)
    ledger_account_key: str = Field(..., max_length=32)
    effective_date: datetime.date
    settlement_item_code: Optional[str] = Field(default=None, max_length=30)
    settlement_desc: Optional[str] = Field(default=None, max_length=100)
    fee_category_group: Optional[str] = Field(default=None, max_length=25)
    revenue_group: Optional[str] = Field(default=None, max_length=25)
    merchant_plan_uuid: Optional[str] = Field(default=None, max_length=13)
    developer_uuid: Optional[str] = Field(default=None, max_length=13)
    developer_app_uuid: Optional[str] = Field(default=None, max_length=13)
    app_subscription_uuid: Optional[str] = Field(default=None, max_length=13)
    app_metered_uuid: Optional[str] = Field(default=None, max_length=13)
    created_timestamp: datetime.datetime
    modified_timestamp: datetime.datetime
    audit_id: Optional[str] = Field(default=None, max_length=26)

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
                "ledger_account_key": "REVENUE_SUBSCRIPTION_MONTHLY",
                "effective_date": "2023-10-27",
                "settlement_item_code": "SUBS_MONTHLY_001",
                "settlement_desc": "Monthly subscription settlement for premium plan",
                "fee_category_group": "SUBSCRIPTION",
                "revenue_group": "PREMIUM",
                "merchant_plan_uuid": "01H8X7Y7Z7Q12",
                "developer_uuid": "01H8X7Y7Z7Q13",
                "developer_app_uuid": "01H8X7Y7Z7Q14",
                "app_subscription_uuid": "01H8X7Y7Z7Q15",
                "app_metered_uuid": None,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGX",
            }
        }

if __name__ == "__main__":
    example_dict = LedgerAccountSettlement.model_json_schema().get("example", {})
    ledger_account_settlement_instance = LedgerAccountSettlement(**example_dict)
    print("----begin example: ledger-account-settlement----")
    print(ledger_account_settlement_instance.model_dump_json(indent=2))
    print("----begin minmal example: ledger-account-settlement----")
    print(json.dumps(ledger_account_settlement_instance.to_minimal_dict(), indent=2))

    print("----end: ledger-account-settlement----")