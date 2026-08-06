import pytest
from references import TreeNode
from prob06 import prob06


def build_kv(values, i=0):
    """level-order list of (key, val) tuples (with None gaps) -> tree"""
    if i >= len(values) or values[i] is None:
        return None
    key, val = values[i]
    return TreeNode(val, build_kv(values, 2 * i + 1), build_kv(values, 2 * i + 2), key=key)


INVENTORY = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"),
             (15, "Aloe"), (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]


@pytest.mark.parametrize("values, budget, expected", [
    (INVENTORY, 50, "Pothos"),      # example 1
    (INVENTORY, 25, "Aloe"),        # example 2
    (INVENTORY, 15, None),          # example 3: nothing strictly below
    (INVENTORY, 100, "ZZ Plant"),   # budget above every price
    ([], 50, None),                 # empty tree
])
def test_prob06(values, budget, expected):
    assert prob06(build_kv(values), budget) == expected
