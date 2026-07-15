import pytest
from prob05 import prob05

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 4, 5], 14),
    ([10], 10),
    ([], 0),
])
def test_prob05(nums, expected):
    assert prob05(nums) == expected
