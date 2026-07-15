import pytest
from references import Node
from prob12 import prob12


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


@pytest.mark.parametrize("values, expected", [
    (["Isabelle", "Saharah", "C.J."], "Isabelle -> Saharah -> C.J."),
    (["Isabelle"], "Isabelle"),  # single node -> just its value, no separator
])
def test_prob12(values, expected):
    assert prob12(build(values)) == expected
