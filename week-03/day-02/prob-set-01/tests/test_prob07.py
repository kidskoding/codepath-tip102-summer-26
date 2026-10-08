import pytest
from prob07 import prob07


@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 2, 4], [4, 2, 1, 3]),
    ([0], [0]),
    # multi-element order is "any valid arrangement", so not asserted exactly
    ([], []),
    ([2], [2]),
    ([1], [1]),
])
def test_prob07(nums, expected):
    assert prob07(nums) == expected
