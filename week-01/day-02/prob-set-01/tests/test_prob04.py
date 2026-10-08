import pytest
from prob04 import prob04


@pytest.mark.parametrize("num, expected", [
    (423, 9),
    (4, 4),
    (0, 0),
])
def test_prob04(num, expected):
    assert prob04(num) == expected
