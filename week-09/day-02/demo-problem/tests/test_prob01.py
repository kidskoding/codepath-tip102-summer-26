import pytest
from references import TreeNode
from prob01 import prob01


EXAMPLE_1 = lambda: TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
LEFT_SKEW = lambda: TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
FULL_4 = lambda: TreeNode(
    1,
    TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7)),
)


@pytest.mark.parametrize("make_root, expected", [
    (EXAMPLE_1, [[3], [20, 9], [15, 7]]),                       # example 1
    (lambda: TreeNode(1), [[1]]),                               # example 2
    (lambda: None, []),                                         # example 3, empty tree
    (LEFT_SKEW, [[1], [2], [3], [4]]),                          # skewed, one node per level
    (FULL_4, [[1], [3, 2], [4, 5, 6, 7], [9, 8]]),              # 4 levels, both flips
])
def test_prob01(make_root, expected):
    assert prob01(make_root()) == expected
