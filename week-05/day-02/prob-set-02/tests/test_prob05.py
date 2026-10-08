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


def nodes(head):
    out = []
    while head:
        out.append(head)
        head = head.next
    return out


@pytest.mark.parametrize("values", [
    ["Mario", "Daisy", "Luigi"],
    ["Mario"],
])
def test_prob05(values):
    original = build(values)
    copy = prob05(original)
    assert to_list(copy) == values
    # no node object may be shared with the original
    assert not {id(n) for n in nodes(copy)} & {id(n) for n in nodes(original)}
    original.value = "Original Mario"
    assert to_list(copy) == values


def test_prob05_empty():
    assert prob05(None) is None
