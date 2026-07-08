from references import Node
from prob12 import chase_list


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def test_prob12():
    head = build(["Spike", "Tom", "Jerry", "Gouda"])
    assert chase_list(head) == "Spike chases Tom chases Jerry chases Gouda"
