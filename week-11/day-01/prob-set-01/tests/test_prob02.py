import copy

import pytest
from prob02 import prob02

GRID = [
    [1, 0, 1, 1, 0],  # Row 0
    [1, 1, 1, 1, 0],  # Row 1
    [0, 0, 1, 1, 0],  # Row 2
    [1, 0, 1, 1, 1],  # Row 3
]


@pytest.mark.parametrize("position, grid, expected", [
    ((0, 0), GRID, True),
    ((0, 4), GRID, True),  # start is infected, but the next step is safe
    ((3, 0), GRID, False),
    ((3, 4), GRID, True),  # already at the safe haven
    ((0, 0), [[1, 0], [0, 1]], False),  # diagonal moves are not allowed
])
def test_prob02(position, grid, expected):
    assert prob02(position, copy.deepcopy(grid)) == expected
