from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalMerchantDetailMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'seasonal',
        'tax_exempt',
        'verified_terms_acceptance',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class MerchantDetail(BaseModel, MinimalMerchantDetailMixin):
    """
    Pydantic V2 model for the `merchant_detail` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    uuid: str = Field(..., max_length=26, description="Unique identifier for the merchant detail.")
    billing_entity_uuid: str = Field(..., max_length=26, description="UUID of the billing entity.")
    seasonal: int = Field(
        default=0,
        description="Indicates seasonal merchant (non-zero/true) or year-round business (0/false)."
    )
    tax_exempt: int = Field(
        default=0,
        description="Indicates tax exempt status (non-zero/true) or subject to taxes (0/false)."
    )
    verified_terms_acceptance: int = Field(
        default=0,
        description="Indicates verified terms acceptance (non-zero/true) or needs verification (0/false)."
    )
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
                "seasonal": 0,
                "tax_exempt": 1,
                "verified_terms_acceptance": 1,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
                "audit_id": "01H8X7Y7Z7QWERTYUIOPASDFGA",
            }
        }

if __name__ == "__main__":
    example_dict = MerchantDetail.model_json_schema().get("example", {})
    merchant_detail_instance = MerchantDetail(**example_dict)
    print("----begin example: merchant-detail----")
    print(merchant_detail_instance.model_dump_json(indent=2))
    print("----begin minmal example: merchant-detail----")
    print(json.dumps(merchant_detail_instance.to_minimal_dict(), indent=2))
    print("----end: merchant-detail----")