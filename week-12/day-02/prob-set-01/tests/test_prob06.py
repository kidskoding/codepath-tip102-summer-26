import pytest
from prob06 import prob06


@pytest.mark.parametrize("graph, expected", [
    ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
    ([[4, 3, 1], [3, 2, 4], [3], [4], []], [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
    ([[1], []], [[0, 1]]),
])
def test_prob06(graph, expected):
    # paths may come back in any order
    assert sorted(prob06(graph)) == sorted(expected)
