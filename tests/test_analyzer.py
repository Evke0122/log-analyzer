from src.analyzer import get_severity


def test_low_severity():
    assert get_severity(3) == "LOW"


def test_medium_severity():
    assert get_severity(5) == "MEDIUM"


def test_high_severity():
    assert get_severity(10) == "HIGH"