import pytest
from references import Node
from prob07 import prob07


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


@pytest.mark.parametrize("values, item, expected", [
    (["Slingshot", "Peaches", "Scarab Beetle"], "Peaches", ["Slingshot", "Scarab Beetle"]),
    (["Slingshot", "Scarab Beetle"], "Triceratops Torso", ["Slingshot", "Scarab Beetle"]),
    (["Slingshot", "Peaches"], "Slingshot", ["Peaches"]),  # remove the head
    (["Peaches", "Peaches"], "Peaches", ["Peaches"]),  # only the first match
    ([], "Peaches", []),
])
def test_prob07(values, item, expected):
    assert to_list(prob07(build(values), item)) == expected
