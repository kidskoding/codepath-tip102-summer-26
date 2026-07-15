import pytest
from prob01 import find_cruise_length


@pytest.mark.parametrize("cruise_lengths, vacation_length, expected", [
    ([9, 10, 11, 12, 13, 14, 15], 13, True),   # example
    ([8, 9, 12, 13, 13, 14, 15], 11, False),   # example
    ([], 5, False),                            # empty
    ([5], 5, True),                            # single match
    ([5], 3, False),                           # single no match
])
def test_prob01(cruise_lengths, vacation_length, expected):
    assert find_cruise_length(cruise_lengths, vacation_length) == expected
