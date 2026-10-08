import pytest
from prob04 import prob04

VENUE = [[1, 2], [0, 3], [0, 4], [1, 5], [2], [3]]


@pytest.mark.parametrize("venue_map, target, expected", [
    (VENUE, 5, [0, 1, 3, 5]),
    (VENUE, 2, [0, 2]),
    (VENUE, 4, [0, 2, 4]),
    (VENUE, 0, [0]),  # already at the entrance
])
def test_prob04(venue_map, target, expected):
    # this venue is a tree, so each target has exactly one path
    assert prob04(venue_map, target) == expected
