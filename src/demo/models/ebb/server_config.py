from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalServerConfigMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'config_key',
        'config_value',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class ServerConfig(BaseModel, MinimalServerConfigMixin):
    """
    Pydantic V2 model for the `server_config` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    config_key: str = Field(..., max_length=127, description="Configuration key.")
    config_value: Optional[str] = Field(default=None, max_length=2000, description="Configuration value.")
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
                "config_key": "billing.default_currency",
                "config_value": "USD",
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = ServerConfig.model_json_schema().get("example", {})
    server_config_instance = ServerConfig(**example_dict)
    print("----begin example: server-config----")
    print(server_config_instance.model_dump_json(indent=2))
    print("----begin minmal example: server-config----")
    print(json.dumps(server_config_instance.to_minimal_dict(), indent=2))
    print("----end: server-config----")