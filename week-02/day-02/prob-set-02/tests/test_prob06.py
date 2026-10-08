import pytest
from prob06 import prob06


@pytest.mark.parametrize("destinations, expected", [
    ([0, 1, 2, 2, 4, 4, 1], 2),
    ([4, 4, 4, 9, 2, 4], 4),
    ([29, 47, 21, 41, 13, 37, 25, 7], -1),
    ([], -1),
])
def test_prob06(destinations, expected):
    assert prob06(destinations) == expected
