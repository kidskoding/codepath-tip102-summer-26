import pytest
from prob04 import prob04


@pytest.mark.parametrize("logs, expected", [
    ([7, 52, 2, 4], 596),
    ([5, 14, 13, 8, 12], 673),
    ([9], 9),
    ([], 0),
])
def test_prob04(logs, expected):
    assert prob04(logs) == expected
