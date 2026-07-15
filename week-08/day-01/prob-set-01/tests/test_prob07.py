import pytest
from references import TreeNode
from prob07 import prob07

bush = TreeNode(4,
                TreeNode(10, TreeNode(5), TreeNode(8)),
                TreeNode(6, None, TreeNode(20)))


@pytest.mark.parametrize("root, threshold, expected", [
    (bush, 6, 38),   # example: 8 + 10 + 20
    (bush, 30, 0),   # example: nothing above 30
    (bush, 0, 53),   # edge: all nodes count (4+10+5+8+6+20)
    (None, 5, 0),    # edge: empty tree
])
def test_prob07(root, threshold, expected):
    assert prob07(root, threshold) == expected
