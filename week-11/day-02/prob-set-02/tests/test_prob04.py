import copy

import pytest
from prob04 import prob04


@pytest.mark.parametrize("land, expected", [
    ([[1, 0, 0], [0, 1, 1], [0, 1, 1]], [[0, 0, 0, 0], [1, 1, 2, 2]]),
    ([[0, 0], [0, 0]], []),
    ([[1, 1], [1, 1]], [[0, 0, 1, 1]]),
    ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], [[0, 0, 0, 0], [0, 2, 0, 2], [2, 0, 2, 0], [2, 2, 2, 2]]),
])
def test_prob04(land, expected):
    # groups may come back in any order
    assert sorted(prob04(copy.deepcopy(land))) == sorted(expected)
