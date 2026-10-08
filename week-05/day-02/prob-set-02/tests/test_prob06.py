import pytest
from references import Node
from prob06 import prob06


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


@pytest.mark.parametrize("values, n, expected", [
    (["Daisy", "Mario", "Toad", "Yoshi"], 3, ["Daisy", "Mario", "Toad"]),
    (["Daisy", "Mario", "Toad", "Yoshi"], 5, ["Daisy", "Mario", "Toad", "Yoshi"]),
    (["Daisy", "Mario"], 0, []),
    ([], 2, []),
])
def test_prob06(values, n, expected):
    assert prob06(build(values), n) == expected
