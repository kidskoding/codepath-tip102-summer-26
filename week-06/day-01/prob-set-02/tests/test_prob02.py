import pytest
from prob02 import prob02, Node


def build(pairs):
    head = None
    for house, score in reversed(pairs):
        head = Node(house, score, head)
    return head


@pytest.mark.parametrize("pairs, score, expected", [
    ([("Gryffindor", 600), ("Ravenclaw", 300), ("Slytherin", 500), ("Hufflepuff", 600)], 600, 2),
    ([("Gryffindor", 600), ("Ravenclaw", 300)], 450, 0),
    ([], 600, 0),
])
def test_prob02(pairs, score, expected):
    assert prob02(build(pairs), score) == expected
