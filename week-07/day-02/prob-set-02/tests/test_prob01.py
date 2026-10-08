import pytest
from prob01 import prob01


@pytest.mark.parametrize("playlist, length, expected", [
    ([101, 102, 103, 104, 105], 103, 2),
    ([201, 202, 203, 204, 205], 206, -1),
    ([201, 202, 203, 204, 205], 201, 0),  # first
    ([201, 202, 203, 204, 205], 205, 4),  # last
    ([], 100, -1),
])
def test_prob01(playlist, length, expected):
    assert prob01(playlist, length) == expected
