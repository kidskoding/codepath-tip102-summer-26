import pytest
from prob02 import prob02


@pytest.mark.parametrize("durations, expected", [
    ([30, 45, 60, 45, 30], 60),
    ([20, 30, 40, 40, 30, 20], 40),
    ([55, 60, 55, 60, 60], 60),
    ([42], 42),
])
def test_prob02(durations, expected):
    assert prob02(durations) == expected
