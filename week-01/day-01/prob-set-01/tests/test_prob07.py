import pytest
from prob07 import count_less_than

@pytest.mark.parametrize("nums, threshold, expected", [
    ([1, 2, 3, 4, 5, 6], 4, 3),
    ([], 4, 0),
    # edge: none below threshold, all below threshold, and strict "<" (equal not counted)
    ([5, 6, 7], 4, 0),
    ([1, 2, 3], 4, 3),
    ([4, 4, 4], 4, 0),
])
def test_prob07(nums, threshold, expected):
    assert count_less_than(nums, threshold) == expected
