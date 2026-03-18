import os
import json
import pytest
from cli.validator import validate_safety_checks

# Sample JSON Files for testing

complete_data = {
    "Hard hats present": True,
    "Scaffoldind inspected": True,
    "Guard rails installed": True,
    "Electrical hazards addressed": True
}

missing_field_data = {
    "Hard hats present": True,
    "Scaffolding inspected": True,
    "Guard rails installed": True
}

invalid_json = "{ not: 'json'}"

def write_temp_file(content, filename="temp.json"):
    with open(filename, "w") as f:
        if isinstance(content, dict):
            json.dump(content, f)
        else:
            f.write(content)
    return filename

# Unit Test 1

def test_complete_data():
    file = write_temp_file(complete_data)
    assert validate_safety_checks(file) == "Pass"
    os.remove(file)

# Unit Test 2

def test_missing_field():
    file = write_temp_file(missing_field_data)
    assert "Fail" in validate_safety_checks(file)
    os.remove(file)

# Unit Test 3

def test_invalid_json():
    file = write_temp_file(invalid_json)
    assert "Fail" in validate_safety_checks(file)
    os.remove(file)