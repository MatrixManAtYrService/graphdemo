from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalPartnerConfigMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'hierarchy_type',
        'revenue_share_group',
        'post_method',
        'invoice_method',
        'settlement_method',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class PartnerConfig(BaseModel, MinimalPartnerConfigMixin):
    """
    Pydantic V2 model for the `partner_config` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the partner config.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    hierarchy_type: str = Field(..., max_length=20, description="Type of billing hierarchy.")
    effective_date: datetime.date = Field(..., description="Date when the configuration becomes effective.")
    revenue_share_group: Optional[str] = Field(default=None, max_length=20, description="Revenue sharing group.")
    post_method: Optional[str] = Field(default=None, max_length=20, description="Posting method.")
    plan_billing_method: Optional[str] = Field(default=None, max_length=20, description="Plan billing method.")
    invoice_method: Optional[str] = Field(default=None, max_length=20, description="Invoicing method.")
    invoice_number_format: Optional[str] = Field(default=None, max_length=20, description="Invoice number format.")
    settlement_method: Optional[str] = Field(default=None, max_length=20, description="Settlement method.")
    seasonal_rule_set_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of seasonal rule set.")
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
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "hierarchy_type": "MERCHANT",
                "effective_date": "2023-11-01",
                "revenue_share_group": "STANDARD",
                "post_method": "IMMEDIATE",
                "plan_billing_method": "PREPAID",
                "invoice_method": "ELECTRONIC",
                "invoice_number_format": "INV-{YYYY}-{SEQ}",
                "settlement_method": "NET30",
                "seasonal_rule_set_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGA",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGB",
            }
        }

if __name__ == "__main__":
    example_dict = PartnerConfig.model_json_schema().get("example", {})
    partner_config_instance = PartnerConfig(**example_dict)
    print("----begin example: partner-config----")
    print(partner_config_instance.model_dump_json(indent=2))
    print("----begin minmal example: partner-config----")
    print(json.dumps(partner_config_instance.to_minimal_dict(), indent=2))
    print("----end: partner-config----")