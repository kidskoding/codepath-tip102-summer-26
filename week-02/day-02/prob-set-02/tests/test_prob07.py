import pytest
from prob07 import prob07


@pytest.mark.parametrize("itinerary, expected", [
    ([2, 1, 3], False),
    ([1, 3, 3, 2], True),
    ([1, 1], True),
    ([1], False),
    ([2, 2, 1], True),
])
def test_prob07(itinerary, expected):
    assert prob07(itinerary) == expected
