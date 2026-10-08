import pytest
from prob07 import prob07


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], 3),
    ([3, 6, 9], 0),
    ([], 0),
])
def test_prob07(nums, expected):
    assert prob07(nums) == expected
