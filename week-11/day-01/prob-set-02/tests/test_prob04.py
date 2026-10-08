import copy

import pytest
from prob04 import prob04


@pytest.mark.parametrize("board, expected", [
    ([["X", "X", "X", "X"],
      ["X", "O", "O", "X"],
      ["X", "X", "O", "X"],
      ["X", "O", "X", "X"]],
     [["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "X", "X", "X"],
      ["X", "O", "X", "X"]]),
    ([["O"]], [["O"]]),  # on the edge, never captured
    ([["X", "O", "X"],
      ["X", "O", "X"],
      ["X", "X", "X"]],
     [["X", "O", "X"],
      ["X", "O", "X"],
      ["X", "X", "X"]]),  # inner 'O' connects to an edge 'O', so it survives
])
def test_prob04(board, expected):
    grid = copy.deepcopy(board)
    result = prob04(grid)
    assert result == expected
    assert grid == expected  # must modify the map in place
