import pytest
from prob06 import next_greater_event


@pytest.mark.parametrize("nums1, nums2, expected", [
    ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
    ([2, 4], [1, 2, 3, 4], [3, -1]),
    ([1], [1, 2], [2]),
    ([2], [1, 2], [-1]),
])
def test_prob06(nums1, nums2, expected):
    assert next_greater_event(nums1, nums2) == expected
