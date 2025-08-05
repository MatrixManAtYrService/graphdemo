from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalBillingEntityConfigMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'hierarchy_type',
        'post_method',
        'plan_billing_method',
        'invoice_method',
        'settlement_method',
        'effective_date',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class BillingEntityConfig(BaseModel, MinimalBillingEntityConfigMixin):
    """
    Pydantic V2 model for the `billing_entity_config` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the billing entity config.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    hierarchy_type: str = Field(..., max_length=20, description="Type of hierarchy.")
    effective_date: datetime.date = Field(..., description="Date when the configuration becomes effective.")
    post_method: Optional[str] = Field(default=None, max_length=20, description="Method for posting, can be null.")
    plan_billing_method: Optional[str] = Field(default=None, max_length=20, description="Method for plan billing, can be null.")
    invoice_method: Optional[str] = Field(default=None, max_length=20, description="Method for invoicing, can be null.")
    settlement_method: Optional[str] = Field(default=None, max_length=20, description="Method for settlement, can be null.")
    seasonal_rule_set_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of seasonal rule set, can be null.")
    created_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was created."
    )
    modified_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the record was last modified."
    )
    audit_id: Optional[str] = Field(default=None, max_length=26, description="Audit identifier, can be null.")

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
                "hierarchy_type": "STANDARD",
                "effective_date": "2023-10-01",
                "post_method": "AUTOMATIC",
                "plan_billing_method": "MONTHLY",
                "invoice_method": "EMAIL",
                "settlement_method": "NET30",
                "seasonal_rule_set_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = BillingEntityConfig.model_json_schema().get("example", {})
    billing_entity_config_instance = BillingEntityConfig(**example_dict)
    print("----begin example: billing-entity-config----")
    print(billing_entity_config_instance.model_dump_json(indent=2))
    print("----begin minmal example: billing-entity-config----")
    print(json.dumps(billing_entity_config_instance.to_minimal_dict(), indent=2))

    print("----end: billing-entity-config----")