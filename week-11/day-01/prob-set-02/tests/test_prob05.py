import copy

import pytest
from prob05 import prob05


@pytest.mark.parametrize("battlefield, expected", [
    ([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]], 7),
    ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 1),
    ([[0, 0], [0, 0]], 0),  # no troops at all
    ([[5]], 5),
    ([[1, 2], [3, 4]], 10),  # everything connected
])
def test_prob05(battlefield, expected):
    assert prob05(copy.deepcopy(battlefield)) == expected
