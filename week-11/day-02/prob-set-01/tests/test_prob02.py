import copy

import pytest
from prob02 import prob02


@pytest.mark.parametrize("city, expected", [
    ([[1, 1, 1], [0, 0, 1], [1, 1, 1]], True),
    ([[1, 0, 0], [1, 1, 0], [0, 1, 1]], True),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], False),  # two paths that share no cell
    ([[1, 1], [1, 1]], False),  # two paths that share no cell
    ([[1, 0], [0, 1]], True),  # already disconnected: zero flips needed
])
def test_prob02(city, expected):
    assert prob02(copy.deepcopy(city)) == expected
