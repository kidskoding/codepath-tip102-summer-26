import pytest

from prob02 import prob02, Node


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


@pytest.mark.parametrize("values, expected", [
    (["SZA", "Jimin", "Sabrina Carpenter", "SZA"], {"SZA": 2, "Jimin": 1, "Sabrina Carpenter": 1}),
    (["SZA"], {"SZA": 1}),          # edge: single node
    ([], {}),                        # edge: empty list
])
def test_prob02(values, expected):
    assert prob02(build(values)) == expected
