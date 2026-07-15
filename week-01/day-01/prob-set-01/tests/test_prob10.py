import pytest
from prob10 import split_haycorns

@pytest.mark.parametrize("n, expected", [
    (6, [1, 2, 3, 6]),
    (1, [1]),
    # edge: prime -> only 1 and itself, perfect square -> middle divisor once
    (7, [1, 7]),
    (4, [1, 2, 4]),
])
def test_prob10(n, expected):
    assert split_haycorns(n) == expected
