import pytest
from prob08 import prob08


@pytest.mark.parametrize("lst1, lst2, expected", [
    (["pooh", "roo", "piglet"], ["piglet", "eeyore", "owl"], ["pooh", "roo", "eeyore", "owl"]),
    (["pooh", "roo"], ["piglet", "eeyore", "owl", "kanga"], ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]),
    (["pooh", "roo", "piglet"], ["pooh", "roo", "piglet"], []),
    ([], [], []),
])
def test_prob08(lst1, lst2, expected):
    assert prob08(lst1, lst2) == expected
