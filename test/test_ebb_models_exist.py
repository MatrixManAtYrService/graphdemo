import subprocess
import json
import pytest
from pathlib import Path


@pytest.mark.parametrize("sql_file", [
    "plan_action.sql", 
    "adjust_action.sql", 
    "adjust_action_fee_code.sql", 
    "adjust_action_type.sql", 
    "adjust_reason.sql", 
    "app_meter_action.sql",
    "app_meter_action_error.sql",
    "app_meter_action_fee_code.sql",
    "app_meter_action_type.sql",
    "app_sub_action.sql",
    "app_sub_action_error.sql",
    "app_sub_action_fee_code.sql",
    "app_sub_action_type.sql",
    "auto_adjust_advice.sql",
    "auto_adjust_qualifier.sql",
    "auto_adjust_rule.sql"
])
def test_ebb_models_exist_and_run(sql_file):
    """Test that each SQL file has a corresponding Python model that runs successfully."""
    base_path = Path("src/demo/models/ebb")
    
    # Get corresponding Python file
    py_file = sql_file.replace(".sql", ".py")
    py_path = base_path / py_file
    
    # Assert Python file exists
    assert py_path.exists(), f"Python model file {py_path} does not exist for {sql_file}"
    
    # Run the Python file using uv
    result = subprocess.run(
        ["uv", "run", "python", str(py_path)],
        capture_output=True,
        text=True,
        cwd=Path.cwd()
    )
    
    # Assert it returned 0 (success)
    assert result.returncode == 0, f"Python file {py_path} failed with return code {result.returncode}. stderr: {result.stderr}"
    
    # Check that output contains two JSON objects between --- markers
    output_lines = result.stdout.strip().split('\n')
    json_sections = []
    in_json_section = False
    current_json = []
    
    for line in output_lines:
        if line.startswith("----begin"):
            # If we were already in a section, save the previous one
            if in_json_section and current_json:
                json_text = '\n'.join(current_json)
                try:
                    json.loads(json_text)
                    json_sections.append(json_text)
                except json.JSONDecodeError:
                    pass
            in_json_section = True
            current_json = []
        elif line.startswith("----end"):
            in_json_section = False
            if current_json:
                json_text = '\n'.join(current_json)
                try:
                    json.loads(json_text)
                    json_sections.append(json_text)
                except json.JSONDecodeError:
                    pass
            current_json = []
        elif in_json_section and line.strip() and not line.startswith("----"):
            current_json.append(line)
    
    # Assert exactly two valid JSON objects were found
    assert len(json_sections) == 2, f"Expected 2 JSON objects between --- markers, found {len(json_sections)} in output: {result.stdout}"