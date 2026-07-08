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
