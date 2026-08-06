import pytest
from references import Node
from prob01 import prob01


def build(values):
    """list -> linked list, returns head"""
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    """linked list -> list, for comparison"""
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], [1, 2, 4, 5]),        # example 1 (odd length)
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 6]),  # example 2 (even: second middle)
    ([1], []),                               # single node -> empty list
    ([1, 2], [1]),                           # two nodes: second middle deleted
])
def test_prob01(values, expected):
    assert to_list(prob01(build(values))) == expected
