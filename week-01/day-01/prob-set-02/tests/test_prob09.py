import pytest
from prob09 import get_odds

@pytest.mark.parametrize("arg, expected", [
    ([1, 2, 3, 4], [1, 3]),
    ([2, 4, 6, 8], []),
    ([], []),
    ([1, 3, 5], [1, 3, 5]),
])
def test_prob09(arg, expected):
    assert get_odds(arg) == expected
