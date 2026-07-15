import pytest
from references import TreeNode
from prob05 import count_leaves

oak1 = TreeNode("Root",
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


@pytest.mark.parametrize("root, expected", [
    (oak1, 3),           # example
    (oak2, 1),           # example
    (TreeNode("A"), 1),  # edge: single node is itself a leaf
    (None, 0),           # edge: empty tree
])
def test_prob05(root, expected):
    assert count_leaves(root) == expected
