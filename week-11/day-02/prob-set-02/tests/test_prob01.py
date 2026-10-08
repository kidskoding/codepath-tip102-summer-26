import copy

import pytest
from prob01 import prob01


@pytest.mark.parametrize("kingdom, expected", [
    ([[1, 1, 1, 1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0, 1, 1, 0],
      [1, 0, 1, 0, 1, 1, 1, 0],
      [1, 0, 0, 0, 0, 1, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 0]], 2),
    ([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]], 1),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1),
    ([[1]], 0),
    ([[0, 0], [0, 0]], 0),  # every town touches the edge
])
def test_prob01(kingdom, expected):
    assert prob01(copy.deepcopy(kingdom)) == expected
