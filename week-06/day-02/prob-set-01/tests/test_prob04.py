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


@pytest.mark.parametrize("known, witness, expected", [
    # known: 1 -> 2 -> 4, witness: 1 -> 3 -> 4  ->  1 -> 1 -> 2 -> 3 -> 4 -> 4
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
])
def test_prob04(known, witness, expected):
    assert to_list(prob04(build(known), build(witness))) == expected
