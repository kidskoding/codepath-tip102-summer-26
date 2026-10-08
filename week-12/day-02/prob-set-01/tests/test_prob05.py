import pytest
from prob05 import prob05


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([5], 0),
    ([2, 4, 1], 2),  # the lowest price comes after the best buy
])
def test_prob05(prices, expected):
    assert prob05(prices) == expected
