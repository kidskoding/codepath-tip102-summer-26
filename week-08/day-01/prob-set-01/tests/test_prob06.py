import pytest
from references import TreeNode
from prob06 import prob06

magnolia = TreeNode("Root",
                    TreeNode("Node1", TreeNode("Leaf1")),
                    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))


@pytest.mark.parametrize("root, expected", [
    (magnolia, ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]),  # example
    (TreeNode("A"), ["A"]),  # edge: single node
    (None, []),              # edge: empty tree
])
def test_prob06(root, expected):
    assert prob06(root) == expected
