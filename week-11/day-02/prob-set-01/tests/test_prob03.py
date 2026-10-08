import pytest
from prob03 import prob03


@pytest.mark.parametrize("grid, expected", [
    ([" /", "/ "], 2),
    ([" /", "  "], 1),
    (["/\\", "\\/"], 5),
    (["  ", "  "], 1),  # no fences
    (["/"], 2),  # one square split in two
])
def test_prob03(grid, expected):
    assert prob03(grid) == expected
