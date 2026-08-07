from src.analyzer import get_severity


def test_low_severity():
    assert get_severity(3) == "LOW"


def test_medium_severity():
    assert get_severity(5) == "MEDIUM"


def test_high_severity():
    assert get_severity(10) == "HIGH"

from src.log_parser import parse_log_line


def test_parse_failed_login():
    line = "2026-08-06 10:16:02 FAILED user=root ip=45.33.12.8"

    result = parse_log_line(line)

    assert result["status"] == "FAILED"
    assert result["username"] == "root"
    assert result["ip"] == "45.33.12.8"