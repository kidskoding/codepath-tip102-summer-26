import pytest
from prob01 import prob01


@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 2, 2, 2, 3], [3, 1, 1, 2, 2, 2]),
    ([2, 3, 1, 3, 2], [1, 3, 3, 2, 2]),
    ([-1, 1, -6, 4, 5, -6, 1, 4, 1], [5, -1, 4, 4, -6, -6, 1, 1, 1]),
    ([], []),
    ([7], [7]),
])
def test_prob01(nums, expected):
    assert prob01(nums) == expected
