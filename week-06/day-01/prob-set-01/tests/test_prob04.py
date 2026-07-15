from prob04 import prob04, Node


def test_prob04():
    song1 = Node("GO!")
    song2 = Node("N95")
    song3 = Node("WIN")
    song4 = Node("ATM")
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song2
    assert prob04(song1) == True
    # edge: empty list has no cycle
    assert prob04(None) == False
    # edge: single node, no cycle
    assert prob04(Node("solo")) == False
    # edge: single node pointing to itself (whole-list cycle)
    self_loop = Node("loop")
    self_loop.next = self_loop
    assert prob04(self_loop) == True
    # edge: multi-node list with no cycle
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    assert prob04(a) == False
