import pytest
from references import TreeNode
from prob05 import prob05


def build_kv(values, i=0):
    """level-order list of (key, val) tuples (with None gaps) -> tree"""
    if i >= len(values) or values[i] is None:
        return None
    key, val = values[i]
    return TreeNode(val, build_kv(values, 2 * i + 1), build_kv(values, 2 * i + 2), key=key)


@pytest.mark.parametrize("values, expected", [
    # example
    ([(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"),
      None, (2, "Spider Plant"), (4, "Hoya Motoskei")],
     [(1, "Pothos"), (2, "Spider Plant"), (3, "Monstera"),
      (4, "Hoya Motoskei"), (5, "Witchcraft Orchid")]),
    ([], []),                                  # empty tree
    ([(1, "Pothos")], [(1, "Pothos")]),        # single node
])
def test_prob05(values, expected):
    assert prob05(build_kv(values)) == expected
