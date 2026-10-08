import pytest
from prob03 import prob03

FLIGHTS = [
    [0, 1, 1, 0, 0],  # Airport 0
    [0, 0, 1, 0, 0],  # Airport 1
    [0, 0, 0, 1, 0],  # Airport 2
    [0, 0, 0, 0, 1],  # Airport 3
    [0, 0, 0, 0, 0],  # Airport 4
]


@pytest.mark.parametrize("i, j, expected", [
    (0, 2, 1),
    (0, 4, 3),
    (4, 0, -1),
    (1, 4, 3),
    (2, 2, 0),  # already there
])
def test_prob03(i, j, expected):
    assert prob03(FLIGHTS, i, j) == expected
