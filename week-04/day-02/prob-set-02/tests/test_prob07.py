import pytest
from prob07 import prob07


@pytest.mark.parametrize("stack, indices, expected", [
    (["Episode1", "Episode2", "Episode3", "Episode4"], [2, 0, 3, 1], ["Episode2", "Episode4", "Episode1", "Episode3"]),
    (["A", "B", "C", "D"], [1, 2, 3, 0], ["D", "A", "B", "C"]),
    (["Alpha", "Beta", "Gamma"], [0, 2, 1], ["Alpha", "Gamma", "Beta"]),
    ([], [], []),
])
def test_prob07(stack, indices, expected):
    assert prob07(stack, indices) == expected
