import pytest
from prob01 import prob01


@pytest.mark.parametrize("movies, k, expected", [
    ([2, 3, 2], 2, 6),
    ([5, 1, 1, 1], 0, 8),
    ([1], 0, 1),
    ([3], 0, 3),
])
def test_prob01(movies, k, expected):
    assert prob01(movies, k) == expected
