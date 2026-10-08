import pytest
from prob07 import prob07


@pytest.mark.parametrize("audiences, expected", [
    ([100, 200, 200, 150, 100, 250], 250),
    ([120, 180, 220, 150, 220], 440),
    ([50], 50),
    ([30, 30, 30], 90),
])
def test_prob07(audiences, expected):
    assert prob07(audiences) == expected
