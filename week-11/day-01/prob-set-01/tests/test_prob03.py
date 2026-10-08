import copy

import pytest
from prob03 import prob03


# cells may come back in any order, so compare sorted
@pytest.mark.parametrize("grid, expected", [
    ([[1, 0, 1, 0, 1],
      [1, 1, 1, 1, 0],
      [0, 0, 1, 0, 0],
      [1, 0, 1, 1, 1]],
     [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]),
    ([[1, 1], [1, 0]], []),  # safe haven itself is infected
    ([[1]], [(0, 0)]),
])
def test_prob03(grid, expected):
    assert sorted(prob03(copy.deepcopy(grid))) == sorted(expected)
