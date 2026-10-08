import pytest
from references import Node
from prob06 import prob06


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
    ([0, 3, 1, 0, 4, 5, 2, 0], [4, 11]),
    ([0, 1, 0, 3, 0, 2, 2, 0], [1, 3, 4]),
    ([0, 7, 0], [7]),
])
def test_prob06(values, expected):
    assert to_list(prob06(build(values))) == expected
