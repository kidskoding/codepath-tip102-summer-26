import pytest
from references import Node
from prob03 import prob03


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
    ([1, 2, 3, 3, 4], [1, 2, 4]),
    ([1, 1, 1, 2, 3], [2, 3]),  # duplicates at the head
    ([1, 2, 2], [1]),  # duplicates at the tail
    ([1, 1], []),
    ([], []),
])
def test_prob03(values, expected):
    assert to_list(prob03(build(values))) == expected
