import pytest
from prob02 import prob02


@pytest.mark.parametrize("flights, expected", [
    ([[1, 2], [0], [0, 3], [2]], True),   # example
    ([[1, 2], [], [0], [2]], False),      # example
    ([], True),                           # edge: no destinations
    ([[]], True),                         # edge: single destination, no flights
    ([[1], []], False),                   # edge: one-way flight only
])
def test_prob02(flights, expected):
    assert prob02(flights) == expected
