import pytest

from references import Node
from prob12 import chase_list


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


@pytest.mark.parametrize("values, expected", [
    (["Spike", "Tom", "Jerry", "Gouda"], "Spike chases Tom chases Jerry chases Gouda"),
    (["Tom"], "Tom"),                          # single node -> just its value, no separator
    (["Tom", "Jerry"], "Tom chases Jerry"),    # two nodes
])
def test_prob12(values, expected):
    assert chase_list(build(values)) == expected
