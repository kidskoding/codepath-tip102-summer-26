import pytest
from prob03 import prob03


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, False),
    (1, False),  # no legal move at all
    (4, True),
    (9, False),
])
def test_prob03(n, expected):
    assert prob03(n) == expected
