from references import Node
from prob06 import prob06


def chain(values):
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    return nodes


def test_prob06_example():
    nodes = chain(["Mystic Falls", "Troll's Bridge", "Elven Arbor", "Fairy Glade"])
    nodes[3].next = nodes[1]
    assert prob06(nodes[0]) == "Troll's Bridge"


def test_prob06_no_cycle():
    nodes = chain(["Mystic Falls", "Troll's Bridge", "Elven Arbor"])
    assert prob06(nodes[0]) is None


def test_prob06_whole_list_cycle():
    nodes = chain(["Mystic Falls", "Troll's Bridge", "Elven Arbor"])
    nodes[2].next = nodes[0]
    assert prob06(nodes[0]) == "Mystic Falls"


def test_prob06_self_loop():
    solo = Node("Mystic Falls")
    solo.next = solo
    assert prob06(solo) == "Mystic Falls"


def test_prob06_empty():
    assert prob06(None) is None
