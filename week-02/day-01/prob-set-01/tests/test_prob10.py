import pytest
from prob10 import prob10


@pytest.mark.parametrize("vip_passes, guests, expected", [
    ("aA", "aAAbbbb", 3),
    ("z", "ZZ", 0),
    ("abc", "", 0),
])
def test_prob10(vip_passes, guests, expected):
    assert prob10(vip_passes, guests) == expected
