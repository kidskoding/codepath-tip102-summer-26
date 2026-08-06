import pytest
from prob08 import prob08


@pytest.mark.parametrize("boarding_passes, expected", [
    ([("JFK", "ATL"), ("SFO", "JFK"), ("ATL", "ORD"), ("LAX", "SFO")],
     ['LAX', 'SFO', 'JFK', 'ATL', 'ORD']),                  # example
    ([("LAX", "DXB"), ("DFW", "JFK"), ("LHR", "DFW"), ("JFK", "LAX")],
     ['LHR', 'DFW', 'JFK', 'LAX', 'DXB']),                  # example
    ([("A", "B")], ['A', 'B']),                             # edge: single flight
])
def test_prob08(boarding_passes, expected):
    assert prob08(boarding_passes) == expected
