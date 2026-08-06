import pytest
from references import TreeNode
from prob04 import prob04


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


@pytest.mark.parametrize("values, name, expected", [
    # example: Aloe goes left of Fiddle Leaf Fig
    (["Money Tree", "Fiddle Leaf Fig", "Snake Plant"], "Aloe",
     ["Money Tree", "Fiddle Leaf Fig", "Snake Plant", "Aloe"]),
    # insert into empty tree -> new node is the root
    ([], "Aloe", ["Aloe"]),
    # insert to the right
    (["Money Tree", "Fiddle Leaf Fig", "Snake Plant"], "Yucca",
     ["Money Tree", "Fiddle Leaf Fig", "Snake Plant", None, None, None, "Yucca"]),
])
def test_prob04(values, name, expected):
    assert to_level_list(prob04(build(values), name)) == expected
