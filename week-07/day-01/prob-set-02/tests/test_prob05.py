import pytest
from prob05 import prob05


@pytest.mark.parametrize("initial_power, n, expected", [
    (5, 3, 40),  # example: 5 -> 10 -> 20 -> 40
    (7, 2, 28),  # example: 7 -> 14 -> 28
    (5, 0, 5),   # edge: doubled zero times is unchanged
    (1, 4, 16),  # edge: 1 -> 2 -> 4 -> 8 -> 16
])
def test_prob05(initial_power, n, expected):
    assert prob05(initial_power, n) == expected
