import pytest
from references import TreeNode
from prob07 import prob07


def build(values, i=0):
    """level-order list (with None gaps) -> tree, returns root"""
    if i >= len(values) or values[i] is None:
        return None
    return TreeNode(values[i], build(values, 2 * i + 1), build(values, 2 * i + 2))


def to_level_list(root):
    """tree -> level-order list with None gaps, trailing Nones stripped"""
    if root is None:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


COLLECTION = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]


@pytest.mark.parametrize("values, name, expected", [
    # example: two children -> replaced by inorder predecessor (Orchid)
    (COLLECTION, "Pilea",
     ["Money Tree", "Hoya", "Orchid", None, "Ivy", None, "ZZ Plant"]),
    # leaf removal
    (COLLECTION, "Ivy",
     ["Money Tree", "Hoya", "Pilea", None, None, "Orchid", "ZZ Plant"]),
    # one child -> replaced by its child
    (COLLECTION, "Hoya",
     ["Money Tree", "Ivy", "Pilea", None, None, "Orchid", "ZZ Plant"]),
    # root with two children -> predecessor (Ivy) takes root's place
    (COLLECTION, "Money Tree",
     ["Ivy", "Hoya", "Pilea", None, None, "Orchid", "ZZ Plant"]),
    # single-node tree -> empty
    (["Money Tree"], "Money Tree", []),
])
def test_prob07(values, name, expected):
    assert to_level_list(prob07(build(values), name)) == expected
