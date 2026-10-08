import pytest
from prob08 import prob08


@pytest.mark.parametrize("n, dislikes, expected", [
    (4, [[1, 2], [1, 3], [2, 4]], True),
    (3, [[1, 2], [1, 3], [2, 3]], False),
    (1, [], True),
    (4, [[1, 2], [3, 4]], True),  # two separate pairs
    (5, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]], False),  # odd cycle
])
def test_prob08(n, dislikes, expected):
    assert prob08(n, dislikes) == expected
