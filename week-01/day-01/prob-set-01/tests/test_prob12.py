import pytest
from prob12 import locate_thistles

@pytest.mark.parametrize("items, expected", [
    (["thistle", "stick", "carrot", "thistle", "eeyore's tail"], [0, 3]),
    (["book", "bouncy ball", "leaf", "red balloon"], []),
    # edge: empty list -> [], single matching element -> [0]
    ([], []),
    (["thistle"], [0]),
])
def test_prob12(items, expected):
    assert locate_thistles(items) == expected
