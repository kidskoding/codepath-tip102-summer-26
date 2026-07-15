import pytest
from prob02 import prob02


@pytest.mark.parametrize("walls, expected", [
    (["outer", ["inner", ["keep", []]]], 4),  # example
    ([], 1),                                   # example: empty list is one wall
    (["a", "b"], 1),                           # edge: no nested lists -> just the outer
    ([[]], 2),                                 # edge: one nested empty list
])
def test_prob02(walls, expected):
    assert prob02(walls) == expected
