import pytest
from references import TreeNode
from prob06 import prob06


REEF = lambda: TreeNode(
    "CoralA",
    TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")),
    TreeNode("CoralC"),
)


@pytest.mark.parametrize("make_root, expected", [
    (REEF, ["CoralA", "CoralB", "CoralD", "CoralE", "CoralC"]),  # example
    (lambda: None, []),                                           # empty tree
    (lambda: TreeNode("CoralA"), ["CoralA"]),                     # single node
])
def test_prob06(make_root, expected):
    assert prob06(make_root()) == expected
