import pytest
from prob06 import is_increasing_path


@pytest.mark.parametrize("path, expected", [
    ([1, 2, 3, 4, 5], True),   # example
    ([3, 5, 2, 8], False),     # example
    ([5], True),               # edge: single element is trivially increasing
    ([1, 1], False),           # edge: equal neighbors are not STRICTLY increasing
])
def test_prob06(path, expected):
    assert is_increasing_path(path) == expected
