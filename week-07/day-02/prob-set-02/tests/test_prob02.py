import pytest
from prob02 import prob02


@pytest.mark.parametrize("tour_dates, available, expected", [
    ([1, 3, 7, 10, 12], 12, True),
    ([1, 3, 7, 10, 12], 5, False),
    ([1, 3, 7, 10, 12], 1, True),
    ([], 5, False),
])
def test_prob02(tour_dates, available, expected):
    assert prob02(tour_dates, available) == expected
