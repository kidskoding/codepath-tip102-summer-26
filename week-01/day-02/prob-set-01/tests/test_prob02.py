import pytest
from prob02 import prob02


# "any number" that is neither min nor max is valid, so check the property, not one value
@pytest.mark.parametrize("nums, has_answer", [
    ([3, 2, 1, 4], True),
    ([1, 2], False),
    ([2, 1, 3], True),
    ([5], False),
])
def test_prob02(nums, has_answer):
    result = prob02(nums)
    if has_answer:
        assert result in nums and min(nums) < result < max(nums)
    else:
        assert result == -1
