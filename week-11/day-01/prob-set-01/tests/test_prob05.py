import copy

import pytest
from prob05 import prob05


@pytest.mark.parametrize("grid, expected", [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 2]], 0),
    ([[1]], -1),  # a safe zone with no zombies ever
    ([[2, 1, 2]], 1),  # two zombie sources spread at the same time
])
def test_prob05(grid, expected):
    assert prob05(copy.deepcopy(grid)) == expected
