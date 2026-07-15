import pytest
from prob09 import prob09

@pytest.mark.parametrize("arg, expected", [
    ([1, 2, 3, 4], [1, 3]),
    ([2, 4, 6, 8], []),
    ([], []),
    ([1, 3, 5], [1, 3, 5]),
])
def test_prob09(arg, expected):
    assert prob09(arg) == expected
