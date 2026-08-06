import pytest
from prob06 import prob06

FLIGHTS = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": [],
}


@pytest.mark.parametrize("flights, start, expected", [
    (FLIGHTS, "Beijing", ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo',
                          'New York', 'Tokyo', 'Reykjavik']),   # example
    (FLIGHTS, "Helsinki", ['Helsinki', 'Cairo', 'New York', 'Reykjavik']),  # example
    (FLIGHTS, "New York", ['New York']),                        # edge: no outgoing flights
    ({"A": ["B"], "B": []}, "A", ['A', 'B']),                   # edge: two-node graph
])
def test_prob06(flights, start, expected):
    assert prob06(flights, start) == expected
