import pytest
from prob05 import prob05


@pytest.mark.parametrize("n, expected", [
    (2, 16),        # example
    (-2, 0.0625),   # example (negative exponent)
    (0, 1),         # base case: anything^0 == 1
])
def test_prob05(n, expected):
    assert prob05(n) == expected
