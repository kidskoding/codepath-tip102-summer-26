import pytest
from prob09 import prob09

@pytest.mark.parametrize("nums, expected", [
    ([2, 4, 6, 8], True),
    ([1, 2, 3, 4], False),
    ([], True),
    # edge: single even, single odd, and 0 counts as even
    ([2], True),
    ([1], False),
    ([0], True),
])
def test_prob09(nums, expected):
    assert prob09(nums) == expected
