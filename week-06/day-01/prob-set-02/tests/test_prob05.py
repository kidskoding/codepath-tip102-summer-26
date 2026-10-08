import pytest
from references import Node
from prob05 import prob05


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


@pytest.mark.parametrize("values, expected", [
    (["Phoenix", "Dragon", "Phoenix"], True),
    (["Werewolf", "Vampire", "Griffin"], False),
    (["Phoenix"], True),
    (["Phoenix", "Dragon", "Dragon", "Phoenix"], True),  # even length
    (["Phoenix", "Dragon"], False),
])
def test_prob05(values, expected):
    assert prob05(build(values)) == expected
