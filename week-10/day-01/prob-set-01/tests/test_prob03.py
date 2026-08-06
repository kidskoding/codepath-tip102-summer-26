import pytest
from prob03 import prob03

FLIGHTS = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
]


@pytest.mark.parametrize("flights, source, expected", [
    (FLIGHTS, 2, [0, 1, 3]),   # example
    (FLIGHTS, 3, []),          # example
    (FLIGHTS, 0, [1, 2]),      # edge: first row
    (FLIGHTS, 1, [0]),         # edge: single neighbor
    ([[0]], 0, []),            # edge: 1x1 matrix, no flights
])
def test_prob03(flights, source, expected):
    assert sorted(prob03(flights, source)) == expected
