from prob06 import prob06, Node


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def test_prob06():
    song_audio = build([5, 3, 1, 2, 5, 1, 2])
    assert prob06(song_audio) == 3
