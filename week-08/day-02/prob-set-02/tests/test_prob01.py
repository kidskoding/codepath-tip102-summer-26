import pytest
from references import TreeNode
from prob01 import prob01


FAMILY_1 = lambda: TreeNode("A", TreeNode("B", None, TreeNode("D")), TreeNode("C"))
FAMILY_2 = lambda: TreeNode(
    "A",
    TreeNode("B", TreeNode("D")),
    TreeNode("C", TreeNode("E"), TreeNode("F", None, TreeNode("G"))),
)
FAMILY_3 = lambda: TreeNode(
    "A",
    TreeNode("B", TreeNode("D", TreeNode("F", TreeNode("H")))),
    TreeNode("C", None, TreeNode("E", None, TreeNode("G", None, TreeNode("I")))),
)


@pytest.mark.parametrize("make_root, expected_sorted", [
    (FAMILY_1, ["D"]),                              # example 1
    (FAMILY_2, ["D", "G"]),                         # example 2
    (FAMILY_3, ["D", "E", "F", "G", "H", "I"]),     # example 3 (any order)
    (lambda: None, []),                             # empty tree
    (lambda: TreeNode("A"), []),                    # single node
])
def test_prob01(make_root, expected_sorted):
    assert sorted(prob01(make_root())) == expected_sorted
