import pytest
from references import Node
from prob08 import merge_missions


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
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),  # example
    ([], [1], [1]),                              # one empty
    ([], [], []),                                # both empty
])
def test_prob08(a_vals, b_vals, expected):
    assert to_list(merge_missions(build(a_vals), build(b_vals))) == expected
