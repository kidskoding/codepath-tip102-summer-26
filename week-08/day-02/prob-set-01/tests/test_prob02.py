import pytest
from references import TreeNode
from prob02 import prob02


def build(values, i=0):
    """level-order list (with None gaps) -> tree, returns root"""
    if i >= len(values) or values[i] is None:
        return None
    return TreeNode(values[i], build(values, 2 * i + 1), build(values, 2 * i + 2))


GARDEN = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]


@pytest.mark.parametrize("values, name, expected", [
    (GARDEN, "Lilac", True),       # example 1
    (GARDEN, "Sunflower", False),  # example 2
    (GARDEN, "Rose", True),        # root
    (GARDEN, "Violet", True),      # leaf
    ([], "Rose", False),           # empty tree
])
def test_prob02(values, name, expected):
    assert prob02(build(values), name) == expected
