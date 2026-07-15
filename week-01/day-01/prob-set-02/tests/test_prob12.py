import pytest
from prob12 import prob12

@pytest.mark.parametrize("arg, expected", [
    (['Joker', 'Queen', 2, 3, 'Ace', 7], ['Joker', 3, 'Queen', 'Ace', 2, 7]),
    ([9, 2, 3, 'Joker', 'Joker', 3, 2, 9], [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]),
    ([10, 10, 2, 2], [10, 2, 10, 2]),
    (['x', 'y'], ['x', 'y']),  # edge: smallest case n=1 (2 elements) -> unchanged
])
def test_prob12(arg, expected):
    assert prob12(arg) == expected
