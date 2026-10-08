import pytest
from prob03 import prob03, Node


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


@pytest.mark.parametrize("values, expected", [
    (["Poison Antidote", "Shrinking Solution", "Trollblood Tincture"], "Shrinking Solution"),
    (["Elixir of Life", "Sleeping Draught", "Babbling Beverage", "Aging Potion"], "Babbling Beverage"),
    (["Felix Felicis"], "Felix Felicis"),
    (["Polyjuice", "Veritaserum"], "Veritaserum"),  # two middles: return the second
])
def test_prob03(values, expected):
    assert prob03(build(values)) == expected
