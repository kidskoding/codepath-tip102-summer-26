import pytest
from prob05 import merge_schedules


@pytest.mark.parametrize("a, b, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
    ("", "", ""),
    ("abc", "", "abc"),
    ("", "xyz", "xyz"),
])
def test_prob05(a, b, expected):
    assert merge_schedules(a, b) == expected
