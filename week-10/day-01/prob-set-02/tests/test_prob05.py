import pytest
from prob05 import prob05


@pytest.mark.parametrize("trust, n, expected", [
    ([[1, 2]], 2, 2),                      # example
    ([[1, 3], [2, 3]], 3, 3),              # example
    ([[1, 3], [2, 3], [3, 1]], 3, -1),     # example: celebrity trusts someone
    ([], 1, 1),                            # edge: lone contestant trusts nobody
    ([[1, 2], [2, 1]], 2, -1),             # edge: mutual trust, no celebrity
    ([[1, 3]], 3, -1),                     # edge: contestant 2 does not trust 3
])
def test_prob05(trust, n, expected):
    assert prob05(trust, n) == expected
