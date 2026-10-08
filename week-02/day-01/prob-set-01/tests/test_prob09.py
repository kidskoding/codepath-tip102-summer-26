import pytest
from prob09 import prob09


@pytest.mark.parametrize("s, t, expected", [
    (["Alice", "Bob", "Charlie"], ["Bob", "Alice", "Charlie"], 2),
    (["Alice", "Bob", "Charlie", "David", "Eve"], ["Eve", "David", "Bob", "Alice", "Charlie"], 12),
    (["Alice", "Bob"], ["Alice", "Bob"], 0),
    ([], [], 0),
])
def test_prob09(s, t, expected):
    assert prob09(s, t) == expected
