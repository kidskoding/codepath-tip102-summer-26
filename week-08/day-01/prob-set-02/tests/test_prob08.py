import pytest
from references import TreeNode
from prob08 import prob08


OCEAN = lambda: TreeNode(
    "Sunlight",
    TreeNode("Twilight", TreeNode("Abyss", TreeNode("Trenches")), TreeNode("Anglerfish")),
    TreeNode("Squid", TreeNode("Giant Squid")),
)
TIDAL_ZONES = lambda: TreeNode(
    "Spray Zone",
    TreeNode("Beach"),
    TreeNode("High Tide", TreeNode("Middle Tide", None, TreeNode("Low Tide"))),
)


@pytest.mark.parametrize("make_root, expected", [
    (OCEAN, 4),                            # example 1
    (TIDAL_ZONES, 4),                      # example 2
    (lambda: None, 0),                     # empty tree
    (lambda: TreeNode("Sunlight"), 1),     # single node
])
def test_prob08(make_root, expected):
    assert prob08(make_root()) == expected
