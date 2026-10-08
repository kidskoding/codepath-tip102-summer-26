import copy

import pytest
from prob03 import prob03

INF = float("inf")


@pytest.mark.parametrize("castle, expected", [
    ([[INF, -1, 0, INF],
      [INF, INF, INF, -1],
      [INF, -1, INF, -1],
      [0, -1, INF, INF]],
     [[3, -1, 0, 1],
      [2, 2, 1, -1],
      [1, -1, 2, -1],
      [0, -1, 3, 4]]),
    ([[INF, -1], [-1, 0]], [[INF, -1], [-1, 0]]),  # room walled off from every gate
    ([[0, INF, INF]], [[0, 1, 2]]),
])
def test_prob03(castle, expected):
    grid = copy.deepcopy(castle)
    result = prob03(grid)
    assert result == expected
    assert grid == expected  # must modify the castle in place
