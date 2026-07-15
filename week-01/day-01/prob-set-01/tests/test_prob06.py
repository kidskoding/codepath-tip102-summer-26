import pytest
from prob06 import prob06

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [2, 4, 6]),
    ([], []),
    ([5], [10]),
    ([-3], [-6]),
])
def test_prob06(nums, expected):
    assert prob06(nums) == expected
