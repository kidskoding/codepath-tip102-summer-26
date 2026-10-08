import copy

import pytest
from prob01 import prob01

BATTLE = [
    ["X", "O", "O", "X", "X"],  # Row 0
    ["O", "O", "O", "X", "X"],  # Row 1
    ["X", "X", "X", "O", "O"],  # Row 2
    ["X", "X", "X", "X", "O"],  # Row 3
    ["O", "O", "O", "X", "O"],  # Row 4
]


# moves may come back in any order, so compare sorted
@pytest.mark.parametrize("battle, row, column, past_moves, expected", [
    (BATTLE, 3, 2, [], [(3, 1), (3, 3), (2, 2)]),
    (BATTLE, 3, 2, [(2, 2), (3, 3), (0, 0)], [(3, 1)]),
    (BATTLE, 0, 4, [], [(0, 3), (1, 4)]),
    (BATTLE, 0, 0, [], []),
    (BATTLE, 0, 4, [(0, 3), (1, 4)], []),  # every valid move already taken
])
def test_prob01(battle, row, column, past_moves, expected):
    assert sorted(prob01(copy.deepcopy(battle), row, column, list(past_moves))) == sorted(expected)
