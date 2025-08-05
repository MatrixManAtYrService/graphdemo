# SQL to Pydantic Model Conversion Strategy

This document outlines the strategy for converting SQL table definitions to Pydantic models in the EBB (Enterprise Billing Backend) system.

## Basic Structure

Each SQL file should have a corresponding Python file with the same base name:
- `table_name.sql` → `table_name.py`

## Model Template

```python
from __future__ import annotations

import datetime
import json
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class MinimalTableNameMixin:
    # NOTE: pick fewer than eight of these from the full list
    # avoid uuids or anything else that is likely to be related to joining this to other tables
    # favor ones that seem fundamental to calculating an amount that will appear on a bill
    # a human can adjust this field later if they want to see more or less
    MINIMAL_FIELDS = {
        'field1',
        'field2',
        # ... core billing-related fields only
    }

    def to_minimal_dict(self) -> dict:
        return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))


class TableName(BaseModel, MinimalTableNameMixin):
    """
    Pydantic V2 model for the `table_name` table.
    """
    # Field definitions based on SQL schema
    # ...

    class Config:
        from_attributes = True
        json_encoders = {
            datetime.datetime: lambda v: v.isoformat(),
            datetime.date: lambda v: v.isoformat(),
        }
        json_schema_extra = {
            "example": {
                # Sample data matching the schema
            }
        }

if __name__ == "__main__":
    example_dict = TableName.model_json_schema().get("example", {})
    table_name_instance = TableName(**example_dict)
    print("----begin example: table-name----")
    print(table_name_instance.model_dump_json(indent=2))
    print("----begin minmal example: table-name----")
    print(json.dumps(table_name_instance.to_minimal_dict(), indent=2))
    print("----end: table-name----")
```

## Key Strategies

### 1. Datetime Handling Strategy

**Problem**: Datetime objects need to be serialized to strings for JSON output, but we want to maintain clean, reusable code.

**Solution**: Use `model_dump_json()` with Pydantic's `json_encoders` in the Config class, then convert back to dict:

```python
def to_minimal_dict(self) -> dict:
    return json.loads(self.model_dump_json(include=self.MINIMAL_FIELDS))
```

This approach:
- Leverages Pydantic's built-in `json_encoders` in the Config class
- Converts datetime objects to ISO format strings automatically
- Returns a clean Python dict with properly serialized values
- Avoids manual datetime conversion logic in each model

### 2. Field Mapping Rules

| SQL Type | Python Type | Notes |
|----------|-------------|-------|
| `bigint unsigned AUTO_INCREMENT` | `int = Field(..., gt=0)` | Primary key |
| `char(N)` | `str = Field(..., max_length=N)` | Fixed length strings |
| `varchar(N)` | `str = Field(..., max_length=N)` | Variable length strings |
| `varchar(N) DEFAULT NULL` | `Optional[str] = Field(default=None, max_length=N)` | Nullable strings |
| `datetime(6)` | `datetime.datetime` | Timestamps |
| `date` | `datetime.date` | Dates only |
| `decimal(M,D)` | `Decimal = Field(max_digits=M, decimal_places=D)` | Precise decimals |
| `smallint` | `int` | Small integers |
| `smallint unsigned` | `int = Field(ge=0)` | Non-negative integers |

### 3. Minimal Fields Selection

For the `MINIMAL_FIELDS` set:
- **Include**: Fields fundamental to billing calculations (amounts, rates, categories, codes)
- **Exclude**: UUIDs used for joins, audit fields, timestamps
- **Limit**: Fewer than 8 fields total
- **Focus**: Fields that would appear on a customer bill or affect billing logic

### 4. Example Data Strategy

Create realistic example data in `json_schema_extra` that:
- Uses proper UUID formats (26-char ULIDs: `01H8X7Y7Z7QWERTYUIOPASDFGH`)
- Includes meaningful business values (e.g., "MONTHLY_FEE", "RECURRING")
- Follows consistent datetime formats (`2023-10-27T10:00:00.123456`)
- Represents realistic billing scenarios

## Testing Requirements

Each model must:
1. Run successfully when executed directly (`python table_name.py`)
2. Return exit code 0
3. Output exactly two JSON objects between `----begin` and `----end` markers
4. Have valid JSON in both the full example and minimal example outputs

## Common Patterns to Handle

### Tables with Audit Fields
- Include `audit_id` as `Optional[str]` 
- Set `default=None` for audit fields

### Tables with Soft Deletes
- Include `deleted_date` as `Optional[datetime.date]`
- Set `default=None`

### Fee-Related Tables
- Common minimal fields: `fee_category`, `fee_code`, amounts, units
- Avoid developer/app UUIDs in minimal sets unless core to billing

## Future Extensibility

As we encounter new patterns or edge cases, document them here with:
1. **Problem**: Description of the issue
2. **Solution**: How to handle it
3. **Example**: Code snippet showing the pattern
4. **Rationale**: Why this approach was chosen