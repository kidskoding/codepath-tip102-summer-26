import pytest
from references import TreeNode
from prob04 import prob04


PEARLS = lambda: TreeNode(
    3,
    TreeNode(1, None, TreeNode(2)),
    TreeNode(5, TreeNode(4), TreeNode(8)),
)


@pytest.mark.parametrize("make_root, expected", [
    (PEARLS, [1, 2, 3, 4, 5, 8]),   # example
    (lambda: None, []),              # empty tree
    (lambda: TreeNode(5), [5]),      # single node
])
def test_prob04(make_root, expected):
    assert prob04(make_root()) == expected
