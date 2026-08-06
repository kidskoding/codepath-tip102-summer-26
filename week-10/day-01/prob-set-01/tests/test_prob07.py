import pytest
from prob07 import prob07

FLIGHTS = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
}


@pytest.mark.parametrize("flights, start, expected", [
    (FLIGHTS, "Beijing", ['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki',
                          'Cairo', 'Reykjavik', 'New York']),   # example
    (FLIGHTS, "Helsinki", ['Helsinki', 'Cairo', 'Reykjavik', 'New York']),  # example
    (FLIGHTS, "New York", ['New York']),                        # edge: not a key in flights
    ({"A": ["B"], "B": []}, "A", ['A', 'B']),                   # edge: two-node graph
])
def test_prob07(flights, start, expected):
    assert prob07(flights, start) == expected
