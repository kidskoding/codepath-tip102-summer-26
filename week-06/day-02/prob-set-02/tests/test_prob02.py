import pytest
from references import Node
from prob02 import prob02


def chain(values, back_to=None):
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if back_to is not None:
        nodes[-1].next = nodes[back_to]
    return nodes[0]


def assert_straight(head, expected):
    # walk exactly len(expected) nodes, so a cycle the solution failed to cut
    # can never send this check around forever
    node = head
    for value in expected:
        assert node is not None and node.value == value
        last, node = node, node.next
    assert last.next is None


@pytest.mark.parametrize("values, back_to", [
    (["Trailhead", "Trail Fork", "The Falls", "Peak"], 1),  # example: Peak -> Trail Fork
    (["Trailhead", "Trail Fork", "The Falls"], 0),  # whole-list loop
    (["Trailhead"], 0),  # single node pointing to itself
    (["Trailhead", "Trail Fork", "The Falls"], None),  # no cycle: unchanged
])
def test_prob02(values, back_to):
    assert_straight(prob02(chain(values, back_to)), values)
