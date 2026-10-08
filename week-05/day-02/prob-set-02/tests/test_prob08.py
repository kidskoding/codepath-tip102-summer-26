import pytest
from references import Player
from prob08 import prob08


def characters(head):
    out = []
    while head:
        out.append(head.value.character)
        head = head.next
    return out


@pytest.mark.parametrize("racers", [
    [("Mario", "Mushmellow"), ("Luigi", "Standard LG"), ("Peach", "Bumble V")],
    [("Peach", "Bumble V")],
])
def test_prob08(racers):
    arr = [Player(c, k) for c, k in racers]
    head = prob08(arr)
    assert characters(head) == [c for c, _ in racers]
    assert head.value is arr[0]  # node values are the Player objects themselves


def test_prob08_empty():
    assert prob08([]) is None
