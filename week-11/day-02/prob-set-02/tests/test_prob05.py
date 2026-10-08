import copy

import pytest
from prob05 import prob05


@pytest.mark.parametrize("grid, row, col, new_strength, expected", [
    ([[1, 1, 1, 2], [1, 3, 1, 2], [1, 1, 1, 2]], 1, 1, 4, [[1, 1, 1, 2], [1, 4, 1, 2], [1, 1, 1, 2]]),
    ([[1, 1], [1, 1]], 0, 0, 5, [[5, 5], [5, 5]]),  # every square is on the edge
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0, 0, 5, [[5, 5, 5], [5, 1, 5], [5, 5, 5]]),  # center is not border
    ([[1, 1, 1, 2], [1, 3, 1, 2], [1, 1, 1, 2]], 0, 3, 9, [[1, 1, 1, 9], [1, 3, 1, 9], [1, 1, 1, 9]]),
])
def test_prob05(grid, row, col, new_strength, expected):
    assert prob05(copy.deepcopy(grid), row, col, new_strength) == expected
