import pytest
from prob04 import prob04


@pytest.mark.parametrize("intervals, expected", [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
    ([], True),
    ([[1, 5], [5, 8]], True),  # one ends exactly when the next starts
])
def test_prob04(intervals, expected):
    assert prob04(intervals) == expected
