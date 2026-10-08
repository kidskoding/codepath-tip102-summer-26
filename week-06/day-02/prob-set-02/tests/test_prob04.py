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


@pytest.mark.parametrize("values, m, n, expected", [
    (list(range(1, 14)), 2, 3, [1, 2, 6, 7, 11, 12]),
    (list(range(1, 11)), 2, 3, [1, 2, 6, 7]),
    ([1, 2, 3], 1, 1, [1, 3]),
    ([1, 2, 3], 5, 1, [1, 2, 3]),  # m longer than the list
])
def test_prob04(values, m, n, expected):
    assert to_list(prob04(build(values), m, n)) == expected
