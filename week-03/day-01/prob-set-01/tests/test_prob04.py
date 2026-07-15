import pytest
from prob04 import engagement_boost

@pytest.mark.parametrize("nums, expected", [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([], []),        # empty input
    ([5], [25]),     # single positive
    ([-3], [9]),     # single negative
])
def test_prob04(nums, expected):
    assert engagement_boost(nums) == expected
