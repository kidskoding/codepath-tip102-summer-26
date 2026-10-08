import pytest
from prob08 import prob08

FLIGHTS = {
    "LAX": ["SFO"],
    "SFO": ["LAX", "ORD", "ERW"],
    "ERW": ["SFO", "ORD"],
    "ORD": ["ERW", "SFO", "MIA"],
    "MIA": ["ORD"],
}


def assert_valid_path(flights, path, source, dest):
    # any valid flight path is accepted, so check the path's properties
    assert path[0] == source and path[-1] == dest
    assert len(path) == len(set(path))  # no airport repeated
    for a, b in zip(path, path[1:]):
        assert b in flights[a]


@pytest.mark.parametrize("source, dest", [
    ("LAX", "MIA"),
    ("MIA", "LAX"),
    ("ERW", "SFO"),
])
def test_prob08(source, dest):
    assert_valid_path(FLIGHTS, prob08(FLIGHTS, source, dest), source, dest)


def test_prob08_same_airport():
    assert prob08(FLIGHTS, "LAX", "LAX") == ["LAX"]
