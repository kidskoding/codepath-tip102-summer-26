import pytest
from prob12 import prob12


@pytest.mark.parametrize("performer_names, performance_times, expected", [
    (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
    (["Alice", "Bob", "Bob"], [155, 185, 150], ["Bob", "Alice", "Bob"]),
    (["Solo"], [60], ["Solo"]),
])
def test_prob12(performer_names, performance_times, expected):
    assert prob12(performer_names, performance_times) == expected
