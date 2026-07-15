import pytest

from prob06 import prob06, Node


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


@pytest.mark.parametrize("values, expected", [
    ([5, 3, 1, 2, 5, 1, 2], 3),
    ([], 0),              # edge: empty list -> no critical points
    ([5], 0),             # edge: single node (head==tail) -> no critical points
    ([1, 2], 0),          # edge: two nodes (both endpoints) -> no critical points
    ([1, 2, 3], 0),       # edge: monotonic three nodes -> no local minima/maxima
    ([1, 3, 2], 1),       # edge: single local maxima
])
def test_prob06(values, expected):
    assert prob06(build(values)) == expected
