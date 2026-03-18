"""
validator.py

Core logic for Beams & Brackets Safety Validator CLI.
Validates JSON safety checklists and return Pass/Fail.

"""

import json

def validate_safety_checks(json_file: str) -> str:
    """
        Function That Validates Safety Checks from a JSON File.

        Args: json_file(str) : Path to JSON file

        Returns: str: "Pass" if all required checks are present, "Fail" otherwise
    """

    try:
        with open(json_file, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        return "Fail: File not found."
    
    except json.JSONDecodeError:
        return "Fail: Invalid JSON."
    
    required_fields = [
        "Hard hats present",
        "Scaffolding inspected",
        "Guard rails installed",
        "Electrical hazards addressed"
    ]

    for field in required_fields:
        if field not in data or not data[field]:
            return f"Fail: '{field}' missing or not True."
        
    return "Pass"
