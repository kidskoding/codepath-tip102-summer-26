import pytest
from prob06 import prob06


@pytest.mark.parametrize("ratings, expected", [
    ([1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0]),
    ([0, 1], [1, 0]),
    ([2, 2, 2, 2], [4, 4, 0, 0]),
])
def test_prob06(ratings, expected):
    assert prob06(ratings) == expected
