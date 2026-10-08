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


@pytest.mark.parametrize("values, task, expected", [
    (["shake tree", "dig fossils", "catch bugs"], "check turnip prices",
     ["check turnip prices", "shake tree", "dig fossils", "catch bugs"]),
    ([], "catch bugs", ["catch bugs"]),
])
def test_prob03(values, task, expected):
    assert to_list(prob03(build(values), task)) == expected
