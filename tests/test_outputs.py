import json
import os
import pytest

SAMPLE_LOG_FILE = "sample.log"

def parse_sample_log():
    """Helper: parse sample.log to know expected fields and levels."""
    expected_entries = []
    with open(SAMPLE_LOG_FILE) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
                
            parts = line.split(" ", 2)
            
            if len(parts) == 3:
                timestamp, level, message = parts
            elif len(parts) == 2:
                timestamp, level = parts
                message = ""
            elif len(parts) == 1:
                timestamp = parts[0]
                level = ""
                message = ""
            else:
                continue
                
            expected_entries.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })
    return expected_entries


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


def test_levels_are_present():
    """Test that levels exist, but don't validate specific values"""
    with open("clean.json") as f:
        data = json.load(f)
    for entry in data:
        assert entry["level"] is not None, "Level must be present"
        assert isinstance(entry["level"], str), "Level must be a string"


def test_number_of_records_matches_sample():
    """Ensure all records from sample.log are in clean.json."""
    expected = parse_sample_log()
    with open("clean.json") as f:
        actual = json.load(f)
    assert len(actual) == len(expected), (
        f"Expected {len(expected)} records but found {len(actual)}"
    )


def test_entries_match_sample_content():
    """Verify each entry in clean.json matches corresponding sample.log entry."""
    expected = parse_sample_log()
    with open("clean.json") as f:
        actual = json.load(f)
    
    assert len(actual) == len(expected), "Number of entries doesn't match"
    
    for i, (e, a) in enumerate(zip(expected, actual)):
        assert e["timestamp"] == a["timestamp"], f"Timestamps do not match at index {i}"
        assert e["level"] == a["level"], f"Levels do not match at index {i}"
        assert e["message"] == a["message"], f"Messages do not match at index {i}"