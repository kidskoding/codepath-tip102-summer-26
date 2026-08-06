import pytest
from references import TreeNode
from prob03 import prob03


@pytest.mark.parametrize("make_root, expected", [
    (lambda: TreeNode("OR", TreeNode(True), TreeNode(False)), True),    # example 1
    (lambda: TreeNode(False), False),                                    # example 2: leaf
    (lambda: TreeNode(True), True),                                      # leaf True
    (lambda: TreeNode("AND", TreeNode(True), TreeNode(False)), False),   # AND
    (lambda: TreeNode("AND", TreeNode(True), TreeNode(True)), True),     # AND both true
    (lambda: TreeNode("OR", TreeNode(False), TreeNode(False)), False),   # OR both false
])
def test_prob03(make_root, expected):
    assert prob03(make_root()) == expected
