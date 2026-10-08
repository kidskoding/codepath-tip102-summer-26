import pytest
from prob05 import prob05

FLIGHTS = {
    "LAX": [("SFO", 50)],
    "SFO": [("LAX", 50), ("ORD", 100), ("ERW", 210)],
    "ERW": [("SFO", 210), ("ORD", 300)],
    "ORD": [("ERW", 300), ("SFO", 100), ("MIA", 400)],
    "MIA": [("ORD", 400)],
}


@pytest.mark.parametrize("flights, start, dest, accepted", [
    (FLIGHTS, "LAX", "MIA", {550, 960}),  # any valid path's cost is accepted
    (FLIGHTS, "LAX", "SFO", {50}),
    (FLIGHTS, "LAX", "LAX", {0}),
    ({"LAX": [("SFO", 50)], "SFO": [], "JFK": []}, "LAX", "JFK", {-1}),  # unreachable
])
def test_prob05(flights, start, dest, accepted):
    assert prob05(flights, start, dest) in accepted
