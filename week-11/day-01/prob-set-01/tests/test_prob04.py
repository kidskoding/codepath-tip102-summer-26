import copy

import pytest
from prob04 import prob04


@pytest.mark.parametrize("grid, expected", [
    ([[0, 0, 0, 1, 1],
      [0, 0, 0, 1, 1],
      [1, 1, 1, 0, 0],
      [1, 1, 1, 1, 0],
      [0, 0, 0, 1, 0]], 8),
    ([[0, 0], [0, 0]], 0),  # no safe zones
    ([[1, 0], [0, 1]], 1),  # diagonal cells are not connected
    ([[1, 1], [1, 1]], 4),
])
def test_prob04(grid, expected):
    assert prob04(copy.deepcopy(grid)) == expected
