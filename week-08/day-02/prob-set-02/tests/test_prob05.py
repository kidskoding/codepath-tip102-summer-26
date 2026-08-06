import pytest
from references import TreeNode
from prob05 import prob05


PEARLS = lambda: TreeNode(
    3,
    TreeNode(1, None, TreeNode(2)),
    TreeNode(5, TreeNode(4), TreeNode(8)),
)


@pytest.mark.parametrize("make_root, min_size, expected", [
    (PEARLS, 3, 4),         # example 1
    (PEARLS, 7, 8),         # example 2
    (PEARLS, 8, None),      # example 3: nothing above
    (PEARLS, 0, 1),         # everything above -> smallest overall
    (lambda: None, 3, None),  # empty tree
])
def test_prob05(make_root, min_size, expected):
    assert prob05(make_root(), min_size) == expected
