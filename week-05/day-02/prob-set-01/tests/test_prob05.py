import pytest
from references import Node
from prob05 import prob05


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
    (["Common Butterfly", "Ladybug", "Scarab Beetle"], ["Common Butterfly", "Ladybug"]),
    (["Ladybug"], []),
    ([], []),
])
def test_prob05(values, expected):
    assert to_list(prob05(build(values))) == expected
