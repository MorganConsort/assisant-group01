import csv
import sys
from pathlib import Path
import pytest

# Add project root directory to sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

CSV_PATH = PROJECT_ROOT / "data" / "offices.csv"

# Import target functions directly from src/assistant/rules.py
from src.assistant.rules import load_offices, reply


def test_csv_file_validity():
    """Verify that data/offices.csv exists, is valid, and contains expected headers and non-empty rows."""
    assert CSV_PATH.exists(), f"CSV file does not exist at {CSV_PATH}"

    with CSV_PATH.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

        expected_headers = ["name", "room", "hours"]
        assert headers is not None, "CSV header line is missing."
        assert all(
            col in headers for col in expected_headers
        ), f"Expected headers {expected_headers}, but got {headers}"

        rows = list(reader)
        assert len(rows) >= 6, f"Expected at least 6 office entries, found {len(rows)}"

        for row_idx, row in enumerate(rows, start=2):
            for field in expected_headers:
                assert (
                    row.get(field) and row[field].strip()
                ), f"Row {row_idx} contains empty or missing value for '{field}'"


def test_lookup_office_faculty_of_it():
    """Test office lookup for 'Faculty of Information Technology'."""
    offices = load_offices(CSV_PATH)
    office_key = "faculty of information technology"

    assert (
        office_key in offices
    ), f"Office '{office_key}' was not found in loaded offices."

    office_data = offices[office_key]
    assert office_data["name"].strip() == "Faculty of Information Technology"
    assert office_data["room"].strip() == "I.604"
    assert "07:00-17:00" in office_data["hours"]


def test_lookup_office_it_helpdesk():
    """Test office lookup for 'IT Helpdesk'."""
    offices = load_offices(CSV_PATH)
    office_key = "it helpdesk"

    assert (
        office_key in offices
    ), f"Office '{office_key}' was not found in loaded offices."

    office_data = offices[office_key]
    assert office_data["name"].strip() == "IT Helpdesk"
    assert office_data["room"].strip() == "E.005"
    assert "08:00-17:00" in office_data["hours"]


def test_reply_function_lookup_new_offices():
    """Test that the reply() function correctly answers queries for newly added offices."""
    offices = load_offices(CSV_PATH)

    # Query 1: Faculty of Information Technology
    response_fit = reply("Where is Faculty of Information Technology?", offices=offices)
    assert "Faculty of Information Technology" in response_fit
    assert "I.604" in response_fit

    # Query 2: IT Helpdesk
    response_it = reply("When is IT Helpdesk open?", offices=offices)
    assert "IT Helpdesk" in response_it
    assert "E.005" in response_it
