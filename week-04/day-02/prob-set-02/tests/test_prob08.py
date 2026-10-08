import pytest
from prob08 import prob08


@pytest.mark.parametrize("timestamps, expected", [
    ([30, 50, 70, 100, 120, 150], 30),
    ([10, 20, 30, 50, 60, 90], 30),
    ([5, 10, 15, 25, 35, 45], 10),
    ([0, 100], 100),
])
def test_prob08(timestamps, expected):
    assert prob08(timestamps) == expected
