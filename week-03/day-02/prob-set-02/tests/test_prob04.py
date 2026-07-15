import pytest
from prob04 import booth_navigation


@pytest.mark.parametrize("actions, expected", [
    ([1, 2, "back", 3, 4], [1, 3, 4]),
    ([5, 3, 2, "back", "back", 7], [5, 7]),
    ([1, "back", 2, "back", "back", 3], [3]),
    ([], []),
    ([1], [1]),
    ([1, "back"], []),
])
def test_prob04(actions, expected):
    assert booth_navigation(actions) == expected
