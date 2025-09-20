import json
import os
import pytest

def test_output_file_created():
    assert os.path.exists("clean.json"), "clean.json was not created"

def test_clean_json_is_valid_json():
    with open("clean.json") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            pytest.fail("clean.json is not valid JSON")

def test_clean_json_is_list():
    with open("clean.json") as f:
        data = json.load(f)
    assert isinstance(data, list), "clean.json must contain a list"

def test_each_entry_has_fields():
    with open("clean.json") as f:
        data = json.load(f)
    for entry in data:
        assert "timestamp" in entry, "Each entry must have timestamp"
        assert "level" in entry, "Each entry must have level"
        assert "message" in entry, "Each entry must have message"

def test_levels_are_valid():
    valid_levels = {"INFO", "WARN", "ERROR"}
    with open("clean.json") as f:
        data = json.load(f)
    for entry in data:
        assert entry["level"] in valid_levels

def test_number_of_records():
    with open("clean.json") as f:
        data = json.load(f)
    assert len(data) >= 1, "At least one record must be present"
