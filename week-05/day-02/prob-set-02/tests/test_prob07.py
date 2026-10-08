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


@pytest.mark.parametrize("values, racer, expected", [
    (["Daisy", "Mario", "Toad", "Mario"], "Mario", ["Daisy", "Toad", "Mario"]),  # first match only
    (["Daisy", "Mario", "Toad"], "Yoshi", ["Daisy", "Mario", "Toad"]),
    (["Daisy", "Mario"], "Daisy", ["Mario"]),  # remove the head
    ([], "Yoshi", []),
])
def test_prob07(values, racer, expected):
    assert to_list(prob07(build(values), racer)) == expected
