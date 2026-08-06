import pytest
from references import TreeNode
from prob07 import prob07


REEF_1 = lambda: TreeNode(
    "Staghorn",
    TreeNode("Sea Fan", TreeNode("Bubble", TreeNode("Fire")), TreeNode("Table")),
    TreeNode("Sea Whip", TreeNode("Star")),
)
REEF_2 = lambda: TreeNode(
    "Fire",
    TreeNode("Black"),
    TreeNode("Star", TreeNode("Lettuce", None, TreeNode("Sea Whip"))),
)


@pytest.mark.parametrize("make_root, expected", [
    (REEF_1, 7),                          # example 1
    (REEF_2, 5),                          # example 2
    (lambda: None, 0),                    # empty tree
    (lambda: TreeNode("Staghorn"), 1),    # single node
])
def test_prob07(make_root, expected):
    assert prob07(make_root()) == expected
