import pytest
from prob08 import prob08


@pytest.mark.parametrize("values, target, expected", [
    ([3.5, 5.4, 7.2, 9.0, 10.5], 8.0, (7.2, 9.0)),
    ([2.0, 4.5, 6.3, 7.8, 12.1], 6.5, (6.3, 7.8)),
    ([1.0, 2.5, 4.0, 6.0, 9.0], 3.0, (2.5, 4.0)),
])
def test_prob08(values, target, expected):
    assert prob08(values, target) == expected
