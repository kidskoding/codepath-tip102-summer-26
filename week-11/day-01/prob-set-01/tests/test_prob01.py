import copy

import pytest
from prob01 import prob01

GRID = [
    [0, 0, 0, 1, 1],  # Row 0
    [0, 0, 0, 1, 1],  # Row 1
    [1, 1, 1, 0, 0],  # Row 2
    [1, 1, 1, 1, 0],  # Row 3
    [0, 0, 0, 1, 0],  # Row 4
]


# moves may come back in any order, so compare sorted
@pytest.mark.parametrize("position, grid, expected", [
    ((3, 2), GRID, [(3, 1), (3, 3), (2, 2)]),
    ((0, 4), GRID, [(0, 3), (1, 4)]),
    ((0, 1), GRID, []),
    ((4, 3), GRID, [(3, 3)]),  # bottom edge: only up is in bounds and safe
    ((0, 0), [[1]], []),  # single cell has no neighbors
])
def test_prob01(position, grid, expected):
    assert sorted(prob01(position, copy.deepcopy(grid))) == sorted(expected)
