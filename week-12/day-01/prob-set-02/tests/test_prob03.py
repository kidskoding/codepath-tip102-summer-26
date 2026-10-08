import pytest
from prob03 import prob03


@pytest.mark.parametrize("steps, expected", [
    ([1, 3, 5, 4, 4, 6], 10),
    ([1, 2, 3, 4, 5], 15),
    ([7], 1),
    ([5, 4, 3], 3),  # only the single-element subarrays
])
def test_prob03(steps, expected):
    assert prob03(steps) == expected
