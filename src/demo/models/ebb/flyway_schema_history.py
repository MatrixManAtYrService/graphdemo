from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalFlywaySchemaHistoryMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'version',
        'description',
        'type',
        'installed_on',
        'success',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class FlywaySchemaHistory(BaseModel, MinimalFlywaySchemaHistoryMixin):
    """
    Pydantic V2 model for the `flyway_schema_history` table.
    """
    installed_rank: int
    version: Optional[str] = Field(default=None, max_length=50)
    description: str = Field(..., max_length=200)
    type: str = Field(..., max_length=20)
    script: str = Field(..., max_length=1000)
    checksum: Optional[int] = Field(default=None)
    installed_by: str = Field(..., max_length=100)
    installed_on: datetime.datetime
    execution_time: int
    success: bool

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                "installed_rank": 1,
                "version": "1.0.0",
                "description": "Create initial billing tables",
                "type": "SQL",
                "script": "V1_0_0__Create_initial_billing_tables.sql",
                "checksum": 123456789,
                "installed_by": "flyway_user",
                "installed_on": "2023-10-27T10:00:00.123456",
                "execution_time": 2500,
                "success": True,
            }
        }

if __name__ == "__main__":
    example_dict = FlywaySchemaHistory.model_json_schema().get("example", {})
    flyway_schema_history_instance = FlywaySchemaHistory(**example_dict)
    print("----begin example: flyway-schema-history----")
    print(flyway_schema_history_instance.model_dump_json(indent=2))
    print("----begin minmal example: flyway-schema-history----")
    print(json.dumps(flyway_schema_history_instance.to_minimal_dict(), indent=2))

    print("----end: flyway-schema-history----")