import copy

import pytest
from prob01 import prob01


@pytest.mark.parametrize("grid, expected", [
    ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
    ([[0]], [[0]]),
    ([[0, 1, 1]], [[0, 1, 2]]),
])
def test_prob01(grid, expected):
    assert prob01(copy.deepcopy(grid)) == expected
