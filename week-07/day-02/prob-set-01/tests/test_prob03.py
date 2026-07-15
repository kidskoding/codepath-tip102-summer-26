import pytest
from prob03 import count_checked_in_passengers


@pytest.mark.parametrize("rooms, expected", [
    ([0, 0, 0, 1, 1, 1, 1], 4),   # example
    ([0, 0, 0, 0, 0, 1], 1),      # example
    ([0, 0, 0, 0, 0, 0], 0),      # example (all zeros)
    ([1, 1, 1], 3),               # all ones
    ([], 0),                      # empty
    ([1], 1),                     # single one
])
def test_prob03(rooms, expected):
    assert count_checked_in_passengers(rooms) == expected
