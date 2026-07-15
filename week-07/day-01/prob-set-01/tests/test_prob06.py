import pytest
from prob06 import strongest_avenger


@pytest.mark.parametrize("strengths, expected", [
    ([88, 92, 95, 99, 97, 100, 94], 100),  # example
    ([50, 75, 85, 60, 90], 90),            # example
    ([7], 7),                              # single element
])
def test_prob06(strengths, expected):
    assert strongest_avenger(strengths) == expected
