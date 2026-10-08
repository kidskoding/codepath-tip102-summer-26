import pytest
from prob01 import prob01


@pytest.mark.parametrize("artists, set_times, expected", [
    (["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"],
     ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"],
     {"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalia": "7:30 PM"}),
    ([], [], {}),
])
def test_prob01(artists, set_times, expected):
    assert prob01(artists, set_times) == expected
