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
    ([5, 6, 7], [6, 7, 8]),
    ([-1], [0]),
    ([], []),
])
def test_prob04(values, expected):
    assert to_list(prob04(build(values))) == expected
