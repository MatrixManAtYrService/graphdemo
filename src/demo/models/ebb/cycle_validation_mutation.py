from __future__ import annotations

import datetime
import json
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MutationAction(str, Enum):
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class TaskType(str, Enum):
    PRODUCER = "PRODUCER"
    CONSUMER = "CONSUMER"


class MinimalCycleValidationMutationMixin:

    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'mutation_action',
        'task_type',
        'validation_group',
        'status',
        'total_count',
        'total_amount',
        'currency',
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class CycleValidationMutation(BaseModel, MinimalCycleValidationMutationMixin):
    """
    Pydantic V2 model for the `cycle_validation_mutation` table.
    """
    id: int = Field(..., description="Primary key, auto-incrementing.", gt=0)
    mutation_action: MutationAction = Field(..., description="Type of mutation action.")
    mutation_timestamp: datetime.datetime = Field(
        default_factory=datetime.datetime.now,
        description="Timestamp when the mutation occurred."
    )
    cycle_validation_id: int = Field(..., description="ID of the related cycle validation record.", gt=0)
    uuid: str = Field(..., max_length=26, description="UUID of the original cycle validation.")
    task_id: Optional[str] = Field(default=None, max_length=126, description="Identifier for the validation task, can be null.")
    task_type: Optional[TaskType] = Field(default=None, description="Type of validation task, can be null.")
    validation_group: Optional[str] = Field(default=None, max_length=126, description="Group for validation, can be null.")
    billing_entity_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the billing entity, can be null.")
    hierarchy_type: Optional[str] = Field(default=None, max_length=20, description="Type of hierarchy, can be null.")
    cycle_date: Optional[datetime.date] = Field(default=None, description="Date of the billing cycle, can be null.")
    currency: Optional[str] = Field(default=None, max_length=3, description="Currency for validation amounts, can be null.")
    status: Optional[str] = Field(default=None, max_length=25, description="Status of the validation, can be null.")
    bypass_count: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=4, description="Count of bypassed items, can be null.")
    bypass_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3, description="Amount of bypassed items, can be null.")
    accepted_count: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=4, description="Count of accepted items, can be null.")
    accepted_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3, description="Amount of accepted items, can be null.")
    total_count: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=4, description="Total count of items, can be null.")
    total_amount: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=3, description="Total amount of items, can be null.")
    request_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the request, can be null.")
    validation_request_uuid: Optional[str] = Field(default=None, max_length=26, description="UUID of the validation request, can be null.")
    created_timestamp: Optional[datetime.datetime] = Field(default=None, description="Original created timestamp, can be null.")
    modified_timestamp: Optional[datetime.datetime] = Field(default=None, description="Original modified timestamp, can be null.")

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                "id": 1,
                "mutation_action": "UPDATE",
                "mutation_timestamp": "2023-10-27T10:00:00.123456",
                "cycle_validation_id": 123,
                "uuid": "01H8X7Y7Z7QWERTYUIOPASDFGH",
                "task_id": "validation-task-2023-10-27",
                "task_type": "CONSUMER",
                "validation_group": "monthly-billing-validation",
                "billing_entity_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGZ",
                "hierarchy_type": "STANDARD",
                "cycle_date": "2023-10-01",
                "currency": "USD",
                "status": "COMPLETED",
                "bypass_count": "5.0000",
                "bypass_amount": "125.500",
                "accepted_count": "995.0000",
                "accepted_amount": "24875.250",
                "total_count": "1000.0000",
                "total_amount": "25000.750",
                "request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGD",
                "validation_request_uuid": "01H8X7Y7Z7QWERTYUIOPASDFGX",
                "created_timestamp": "2023-10-27T09:00:00.123456",
                "modified_timestamp": "2023-10-27T09:30:00.123456",
            }
        }

if __name__ == "__main__":
    example_dict = CycleValidationMutation.model_json_schema().get("example", {})
    cycle_validation_mutation_instance = CycleValidationMutation(**example_dict)
    print("----begin example: cycle-validation-mutation----")
    print(cycle_validation_mutation_instance.model_dump_json(indent=2))
    print("----begin minmal example: cycle-validation-mutation----")
    print(json.dumps(cycle_validation_mutation_instance.to_minimal_dict(), indent=2))

    print("----end: cycle-validation-mutation----")