import pytest
from prob03 import prob03


@pytest.mark.parametrize("schedule, expected", [
    ("abbaca", "ca"),
    ("azxxzy", "ay"),
    ("aa", ""),
    ("abc", "abc"),
])
def test_prob03(schedule, expected):
    assert prob03(schedule) == expected
