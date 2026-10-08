import pytest
from prob03 import prob03


@pytest.mark.parametrize("x, expected", [
    (4, 2),
    (8, 2),
    (0, 0),
    (1, 1),
    (15, 3),
    (16, 4),
])
def test_prob03(x, expected):
    assert prob03(x) == expected
