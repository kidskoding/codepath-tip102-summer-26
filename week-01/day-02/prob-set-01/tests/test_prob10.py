import pytest
from prob10 import prob10


@pytest.mark.parametrize("pile1, pile2, k, expected", [
    ([1, 3, 4], [1, 3, 4], 1, 5),
    ([1, 2, 4, 12], [2, 4], 3, 2),
    ([], [1, 2], 1, 0),
])
def test_prob10(pile1, pile2, k, expected):
    assert prob10(pile1, pile2, k) == expected
