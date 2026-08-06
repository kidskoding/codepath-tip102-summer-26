import pytest
from references import TreeNode
from prob07 import prob07


@pytest.mark.parametrize("make_root, expected", [
    # example
    (lambda: TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, None, TreeNode(8))), 1),
    # two nodes
    (lambda: TreeNode(1, None, TreeNode(10)), 9),
    # min diff not adjacent to root
    (lambda: TreeNode(5, TreeNode(3), TreeNode(8)), 2),
])
def test_prob07(make_root, expected):
    assert prob07(make_root()) == expected
