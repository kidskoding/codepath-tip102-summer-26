import pytest
from references import TreeNode
from prob03 import prob03

ivy1 = TreeNode("Root",
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


@pytest.mark.parametrize("root, expected", [
    (ivy1, ["Root", "Node2", "Leaf3"]),  # example
    (ivy2, ["Root"]),                     # example: no right child anywhere
    (TreeNode("A"), ["A"]),               # edge: single node
])
def test_prob03(root, expected):
    assert prob03(root) == expected
