import pytest
from prob07 import prob07


@pytest.mark.parametrize("gain, expected", [
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0),
    ([], 0),
])
def test_prob07(gain, expected):
    assert prob07(gain) == expected
