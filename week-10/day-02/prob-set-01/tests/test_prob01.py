import pytest
from prob01 import prob01

FLIGHTS1 = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
FLIGHTS2 = [[0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


@pytest.mark.parametrize("flights, source, dest, expected", [
    (FLIGHTS1, 0, 2, True),
    (FLIGHTS2, 0, 2, False),
    (FLIGHTS1, 2, 0, False),  # flights are one-way
    (FLIGHTS1, 1, 1, True),  # already there
    ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], 0, 2, False),  # cycle that never reaches dest
])
def test_prob01(flights, source, dest, expected):
    assert prob01(flights, source, dest) == expected
