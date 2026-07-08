from references import Node
from prob12 import print_list


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def test_prob12():
    head = build(["Isabelle", "Saharah", "C.J."])
    assert print_list(head) == "Isabelle -> Saharah -> C.J."
