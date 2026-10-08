import pytest
from references import Node
from prob01 import prob01


def loop(values):
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    nodes[-1].next = nodes[0]  # last marker points back to the first
    return nodes[0]


@pytest.mark.parametrize("values", [
    ["Marker 1", "Marker 2", "Marker 3"],
    ["Marker 1"],  # single marker pointing to itself
    ["Marker 1", "Marker 2"],
])
def test_prob01(values):
    assert prob01(loop(values)) == len(values)
