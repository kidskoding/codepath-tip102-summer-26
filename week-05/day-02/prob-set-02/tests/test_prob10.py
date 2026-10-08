import pytest
from references import Node
from prob10 import prob10


def build_doubly(values):
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
        b.prev = a
    return nodes


@pytest.mark.parametrize("values, start", [
    (["Yoshi Falls", "Moo Moo Farm", "Rainbow Road", "DK Mountain"], 2),  # example: start mid-list
    (["Yoshi Falls", "Moo Moo Farm", "Rainbow Road", "DK Mountain"], 0),  # start at head
    (["Yoshi Falls", "Moo Moo Farm", "Rainbow Road", "DK Mountain"], 3),  # start at tail
    (["Rainbow Road"], 0),
])
def test_prob10(values, start):
    assert prob10(build_doubly(values)[start]) == len(values)
