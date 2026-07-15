import pytest
from prob04 import prob04

@pytest.mark.parametrize("items, index, expected", [
    (["piglet", "pooh", "roo", "rabbit"], 0, "piglet"),
    (["piglet", "pooh", "roo", "rabbit"], 2, "roo"),
    (["piglet", "pooh", "roo", "rabbit"], 3, "rabbit"),
    (["piglet", "pooh", "roo", "rabbit"], 10, None),
    ([], 0, None),
    # edge: index exactly at len (just past last valid index) -> None
    (["piglet", "pooh", "roo", "rabbit"], 4, None),
])
def test_prob04(items, index, expected):
    assert prob04(items, index) == expected
