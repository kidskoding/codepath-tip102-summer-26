import pytest
from references import Node
from prob08 import prob08


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
    (["A", "C", "E"], ["B", "D", "F"], ["A", "B", "C", "D", "E", "F"]),  # example
    (["A", "C", "E"], ["B"], ["A", "B", "C", "E"]),  # edge: a longer, b's tail exhausted
    ([], ["X"], ["X"]),                              # edge: one empty
    ([], [], []),                                    # edge: both empty
])
def test_prob08(a_vals, b_vals, expected):
    assert to_list(prob08(build(a_vals), build(b_vals))) == expected
