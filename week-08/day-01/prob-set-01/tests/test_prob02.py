import pytest
from references import TreeNode
from prob02 import calculate_yield


@pytest.mark.parametrize("root, expected", [
    (TreeNode("+", TreeNode(7), TreeNode(5)), 12),  # example
    (TreeNode("*", TreeNode(3), TreeNode(4)), 12),  # edge: multiply
    (TreeNode("-", TreeNode(7), TreeNode(5)), 2),   # edge: subtract
])
def test_prob02(root, expected):
    assert calculate_yield(root) == expected
