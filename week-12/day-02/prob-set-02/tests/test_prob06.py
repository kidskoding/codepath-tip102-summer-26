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


@pytest.mark.parametrize("values, k, expected", [
    ([1, 2, 3], 5, [[1], [2], [3], [], []]),
    (list(range(1, 11)), 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
    ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
    ([], 3, [[], [], []]),
])
def test_prob06(values, k, expected):
    parts = prob06(build(values), k)
    assert len(parts) == k
    assert [to_list(p) for p in parts] == expected
