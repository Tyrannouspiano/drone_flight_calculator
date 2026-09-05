import pytest
from flight_calculator import calculate_flight_time


def test_zero_weight():
    assert calculate_flight_time(0) == 180

def test_positive_weight():
    assert calculate_flight_time(500) == 130

def test_maximum_valid_weight():
    assert calculate_flight_time(1800) == 0

def test_negative_weight_raises_value_error():
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_flight_time(-1)

def test_weight_above_limit_returns_zero():
    assert calculate_flight_time(1801) == 0
