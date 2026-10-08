import pytest
from references import Node
from prob08 import prob08


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
    (["Daisy", "Mario", "Toad", "Peach"], ["Peach", "Daisy", "Mario", "Toad"]),
    (["Daisy", "Mario"], ["Mario", "Daisy"]),
    (["Daisy"], ["Daisy"]),
])
def test_prob08(values, expected):
    assert to_list(prob08(build(values))) == expected
