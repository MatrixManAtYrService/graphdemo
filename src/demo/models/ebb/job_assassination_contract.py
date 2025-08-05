from __future__ import annotations

import datetime
import json
from typing import Optional

from pydantic import BaseModel, Field


class MinimalJobAssassinationContractMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'job_identifier',
        'killed',
        'created_timestamp',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class JobAssassinationContract(BaseModel, MinimalJobAssassinationContractMixin):
    """
    Pydantic V2 model for the `job_assassination_contract` table.
    """
    id: int = Field(..., gt=0)
    job_identifier: str = Field(..., max_length=50)
    killed: int = Field(default=0, ge=0)
    created_timestamp: datetime.datetime
    modified_timestamp: datetime.datetime

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                "id": 1,
                "job_identifier": "BILLING_JOB_01H8X7Y7Z7QWER",
                "killed": 0,
                "created_timestamp": "2023-10-27T10:00:00.123456",
                "modified_timestamp": "2023-10-27T10:00:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = JobAssassinationContract.model_json_schema().get("example", {})
    job_assassination_contract_instance = JobAssassinationContract(**example_dict)
    print("----begin example: job-assassination-contract----")
    print(job_assassination_contract_instance.model_dump_json(indent=2))
    print("----begin minmal example: job-assassination-contract----")
    print(json.dumps(job_assassination_contract_instance.to_minimal_dict(), indent=2))
    print("----end: job-assassination-contract----")