import pytest
from references import TreeNode
from prob02 import prob02


@pytest.mark.parametrize("make_root, expected", [
    (lambda: TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral")), True),    # example 1
    (lambda: TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral")), False),   # example 2
    (lambda: TreeNode("Merenby", None, TreeNode("Calypso")), False),                # example 3: one child
    (lambda: TreeNode("Merenby"), False),                                            # no children
])
def test_prob02(make_root, expected):
    assert prob02(make_root()) == expected
