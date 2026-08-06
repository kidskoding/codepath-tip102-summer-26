import pytest
from references import TreeNode
from prob04 import prob04


SYSTEM_A = lambda: TreeNode(
    "CaveA",
    TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")),
    TreeNode("CaveC", None, TreeNode("CaveF")),
)
SYSTEM_B = lambda: TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))


@pytest.mark.parametrize("make_root, expected", [
    (SYSTEM_A, ["CaveA", "CaveB", "CaveD"]),   # example 1
    (SYSTEM_B, ["CaveA"]),                      # example 2: no left child
    (lambda: TreeNode("CaveA"), ["CaveA"]),     # single node
])
def test_prob04(make_root, expected):
    assert prob04(make_root()) == expected
