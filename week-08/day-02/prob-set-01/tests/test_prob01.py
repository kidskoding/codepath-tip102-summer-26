import pytest
from references import TreeNode
from prob01 import prob01


def build(values, i=0):
    """level-order list (with None gaps) -> tree, returns root"""
    if i >= len(values) or values[i] is None:
        return None
    return TreeNode(values[i], build(values, 2 * i + 1), build(values, 2 * i + 2))


@pytest.mark.parametrize("values, expected", [
    ([2, 3, 5, 6, 7, None, 12], 3),  # example 1
    ([], 0),                          # example 2: empty tree
    ([2], 0),                         # single node, even
    ([3], 1),                         # single node, odd
])
def test_prob01(values, expected):
    assert prob01(build(values)) == expected
