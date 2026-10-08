import pytest
from prob02 import prob02


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([5], 0),  # one day: no trade possible
    ([2, 4, 1], 2),  # the later low comes too late to use
])
def test_prob02(prices, expected):
    assert prob02(prices) == expected
