import pytest
from references import TreeNode
from prob08 import find_flower

field = TreeNode("Rose",
                 TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                 TreeNode("Daisy", None, TreeNode("Dahlia")))


@pytest.mark.parametrize("root, flower, expected", [
    (field, "Lilac", True),      # example
    (field, "Hibiscus", False),  # example
    (field, "Rose", True),       # edge: value at the root
    (None, "Rose", False),       # edge: empty tree
])
def test_prob08(root, flower, expected):
    assert find_flower(root, flower) == expected
