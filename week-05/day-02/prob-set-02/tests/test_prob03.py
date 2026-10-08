import pytest
from references import Node
from prob03 import prob03


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


@pytest.mark.parametrize("values, val, expected", [
    (["banana", "blue shell", "bullet bill"], "red shell", ["banana", "red shell", "blue shell", "bullet bill"]),
    (["banana"], "red shell", ["banana", "red shell"]),
])
def test_prob03(values, val, expected):
    assert to_list(prob03(build(values), val)) == expected
