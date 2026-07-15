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


@pytest.mark.parametrize("values, k, expected", [
    # 1 -> 2 -> 3 -> 4 -> 5, k = 2  ->  4 -> 5 -> 1 -> 2 -> 3
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    # 0 -> 1 -> 2, k = 4  ->  2 -> 0 -> 1
    ([0, 1, 2], 4, [2, 0, 1]),
    # k = 0 -> unchanged
    ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
    # k > len (wrap-around): len 5, k = 7 -> effective 2 -> 4 -> 5 -> 1 -> 2 -> 3
    ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
    # single node, any k -> unchanged
    ([9], 3, [9]),
])
def test_prob05(values, k, expected):
    assert to_list(prob05(build(values), k)) == expected
