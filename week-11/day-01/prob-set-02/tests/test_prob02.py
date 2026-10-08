import copy

import pytest
from prob02 import prob02

KINGDOM = [
    ["X", "O", "X", "X", "O"],  # Row 0
    ["X", "X", "X", "X", "O"],  # Row 1
    ["O", "O", "X", "X", "O"],  # Row 2
    ["X", "O", "X", "X", "X"],  # Row 3
]
CASTLE = (3, 4)


def assert_shortest_path(kingdom, path, town, castle, length):
    # several shortest paths may exist, so check the path's properties
    assert path[0] == town and path[-1] == castle
    assert len(path) == length
    for r, c in path:
        assert kingdom[r][c] == "X"
    for (r1, c1), (r2, c2) in zip(path, path[1:]):
        assert abs(r1 - r2) + abs(c1 - c2) == 1


@pytest.mark.parametrize("town, length", [
    ((0, 0), 8),  # example: e.g. (0,0) -> (1,0) -> (1,1) -> (1,2) -> (2,2) -> (3,2) -> (3,3) -> (3,4)
    ((0, 2), 6),
])
def test_prob02_path(town, length):
    path = prob02(copy.deepcopy(KINGDOM), town, CASTLE)
    assert_shortest_path(KINGDOM, path, town, CASTLE, length)


@pytest.mark.parametrize("town", [
    (0, 4),  # bandit town
    (3, 0),  # cut off
])
def test_prob02_none(town):
    assert prob02(copy.deepcopy(KINGDOM), town, CASTLE) is None


def test_prob02_already_there():
    assert prob02(copy.deepcopy(KINGDOM), CASTLE, CASTLE) == [CASTLE]
