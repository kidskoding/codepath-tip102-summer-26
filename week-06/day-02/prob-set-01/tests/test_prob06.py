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


@pytest.mark.parametrize("a_vals, b_vals, expected", [
    # head_a: 2 -> 4 -> 3 (342), head_b: 5 -> 6 -> 4 (465)  ->  7 -> 0 -> 8 (807)
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    # 5 + 5 = 10 -> 0 -> 1  (final carry produces a new node)
    ([5], [5], [0, 1]),
    # 99 + 1 = 100 -> 0 -> 0 -> 1  (carry propagates past the shorter number)
    ([9, 9], [1], [0, 0, 1]),
])
def test_prob06(a_vals, b_vals, expected):
    assert to_list(prob06(build(a_vals), build(b_vals))) == expected
