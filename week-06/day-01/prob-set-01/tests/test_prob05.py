from prob05 import prob05, Node


def test_prob05():
    song1 = Node("Wein")
    song2 = Node("Si Ai")
    song3 = Node("Qalbi")
    song4 = Node("La")
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song2
    assert prob05(song1) == 3
    # edge: no cycle -> length 0
    assert prob05(None) == 0
    assert prob05(Node("solo")) == 0
    a = Node("a")
    b = Node("b")
    a.next = b
    assert prob05(a) == 0
    # edge: single node self-loop -> cycle length 1
    self_loop = Node("loop")
    self_loop.next = self_loop
    assert prob05(self_loop) == 1
