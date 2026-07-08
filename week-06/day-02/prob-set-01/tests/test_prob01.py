from prob01 import prob01, Node


def test_prob01():
    # clue1 -> clue2 -> clue3 -> clue1  (circular)
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    c.next = a
    assert prob01(a) == True
