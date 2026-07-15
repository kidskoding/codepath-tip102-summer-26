import pytest
from prob02 import sum_stones


@pytest.mark.parametrize("stones, expected", [
    ([5, 10, 15, 20, 25, 30], 105),  # example
    ([12, 8, 22, 16, 10], 68),       # example
    ([], 0),                          # empty
    ([7], 7),                         # single
])
def test_prob02(stones, expected):
    assert sum_stones(stones) == expected
