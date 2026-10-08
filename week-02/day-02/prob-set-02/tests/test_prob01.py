import pytest
from prob01 import prob01


@pytest.mark.parametrize("destinations, rating_threshold, expected", [
    ({"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}, 4.0, {"Paris": 4.8, "Addis Ababa": 4.9}),
    ({"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}, 4.9, {}),
    ({"Paris": 4.0}, 4.0, {"Paris": 4.0}),  # equal to threshold is not strictly below, so kept
    ({}, 4.0, {}),
])
def test_prob01(destinations, rating_threshold, expected):
    assert prob01(destinations, rating_threshold) == expected
