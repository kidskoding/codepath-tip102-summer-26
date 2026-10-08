import pytest
from prob02 import prob02


@pytest.mark.parametrize("cost, expected", [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([5, 10], 5),  # start at step 0, jump two to the top
    ([0, 0, 0], 0),
])
def test_prob02(cost, expected):
    assert prob02(cost) == expected
