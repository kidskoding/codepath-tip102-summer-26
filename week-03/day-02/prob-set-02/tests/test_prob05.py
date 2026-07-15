import pytest
from prob05 import prob05


@pytest.mark.parametrize("a, b, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
    ("", "", ""),
    ("abc", "", "abc"),
    ("", "xyz", "xyz"),
])
def test_prob05(a, b, expected):
    assert prob05(a, b) == expected
