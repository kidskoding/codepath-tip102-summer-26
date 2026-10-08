import pytest
from prob04 import prob04


@pytest.mark.parametrize("durations, expected", [
    ([45, 30, 60, 30, 90], 45),
    ([90, 80, 60, 70, 50], 70),
    ([30, 10, 20, 40, 30, 50], 30.0),
    ([42], 42),
    ([10, 20], 15.0),
])
def test_prob04(durations, expected):
    assert prob04(durations) == expected
