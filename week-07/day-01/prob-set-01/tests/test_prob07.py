import pytest
from prob07 import count_deposits


@pytest.mark.parametrize("resources, expected", [
    ("VVVVV", 5),     # example
    ("VXVYGA", 2),    # example
    ("", 0),          # empty
    ("GXYZ", 0),      # no vibranium
    ("V", 1),         # single deposit
])
def test_prob07(resources, expected):
    assert count_deposits(resources) == expected
