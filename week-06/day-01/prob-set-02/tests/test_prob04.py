import pytest
from references import Node
from prob04 import prob04


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


@pytest.mark.parametrize("values, expected", [
    (["Potion Brewing", "Spell Casting", "Wand Making", "Dragon Taming", "Broomstick Flying"],
     ["Broomstick Flying", "Dragon Taming", "Wand Making", "Spell Casting", "Potion Brewing"]),
    (["Spell Casting", "Wand Making"], ["Wand Making", "Spell Casting"]),
    (["Wand Making"], ["Wand Making"]),
    ([], []),
])
def test_prob04(values, expected):
    assert to_list(prob04(build(values))) == expected
