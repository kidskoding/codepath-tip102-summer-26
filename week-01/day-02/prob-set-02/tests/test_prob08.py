import pytest
from prob08 import prob08


@pytest.mark.parametrize("nums, expected", [
    ([10, 4, 8, 3], [-15, -1, 11, 22]),
    ([1], [0]),
])
def test_prob08(nums, expected):
    assert prob08(nums) == expected
