import copy

import pytest
from prob04 import prob04


@pytest.mark.parametrize("safety, expected", [
    ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
     [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
    ([[2, 1], [1, 2]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
    ([[1]], [[0, 0]]),  # a single subzone touches both oceans
])
def test_prob04(safety, expected):
    # coordinates may come back in any order (as lists or tuples)
    result = prob04(copy.deepcopy(safety))
    assert sorted(list(p) for p in result) == sorted(expected)
