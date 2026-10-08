import copy

import pytest
from prob03 import prob03

DUNGEON = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]


@pytest.mark.parametrize("dungeon, position, exit, expected", [
    (DUNGEON, (0, 4), (4, 4), True),
    (DUNGEON, (0, 4), (3, 2), False),  # can pass through but never stop
    (DUNGEON, (0, 4), (4, 0), True),
    ([[0, 0, 0]], (0, 0), (0, 1), False),  # always rolls past the middle
])
def test_prob03(dungeon, position, exit, expected):
    assert prob03(copy.deepcopy(dungeon), position, exit) == expected
