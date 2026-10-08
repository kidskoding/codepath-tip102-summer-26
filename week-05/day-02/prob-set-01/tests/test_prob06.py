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
    ([5, 6, 7, 8], 5),
    ([8, 5, 6, 7], 5),
    ([3], 3),
    ([4, -2, 9], -2),
])
def test_prob06(values, expected):
    assert prob06(build(values)) == expected
