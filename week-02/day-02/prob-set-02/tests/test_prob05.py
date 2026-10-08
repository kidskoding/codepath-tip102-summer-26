import pytest
from prob05 import prob05


@pytest.mark.parametrize("trips, start_dest, end_dest, expected", [
    ([[1, 2], [3, 4], [5, 6]], 2, 5, True),
    ([[1, 10], [10, 20]], 21, 21, False),
    ([[1, 2], [3, 5]], 2, 5, True),
    ([[1, 2], [4, 5]], 1, 5, False),  # gap at 3
])
def test_prob05(trips, start_dest, end_dest, expected):
    assert prob05(trips, start_dest, end_dest) == expected
