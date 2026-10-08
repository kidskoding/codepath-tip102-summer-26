import pytest
from prob07 import prob07


@pytest.mark.parametrize("flights, expected", [
    ({"JFK": ["LAX", "SFO"], "LAX": ["JFK", "SFO"], "SFO": ["JFK", "LAX"], "ORD": ["ATL"], "ATL": ["ORD"]}, 1),
    ({"JFK": ["LAX"], "LAX": ["JFK"]}, 0),  # already connected
    ({"JFK": [], "LAX": [], "SFO": []}, 2),  # three isolated airports
])
def test_prob07(flights, expected):
    assert prob07(flights) == expected
