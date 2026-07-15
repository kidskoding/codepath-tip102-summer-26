import pytest
from prob07 import longest_streak


@pytest.mark.parametrize("challenges, expected", [
    ("SSOSSS", 3),      # example
    ("SOSOSOSO", 1),    # example
    ("", 0),            # edge: no challenges
    ("OOO", 0),         # edge: no successes
    ("SSSS", 4),        # edge: all successes
])
def test_prob07(challenges, expected):
    assert longest_streak(challenges) == expected
