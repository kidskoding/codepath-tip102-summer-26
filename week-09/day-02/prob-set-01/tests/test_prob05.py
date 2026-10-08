import pytest
from references import TreeNode
from prob05 import prob05


def build(values):
    """CodePath-style level-order list (None = no node) -> tree"""
    if not values:
        return None
    it = iter(values[1:])
    root = TreeNode(values[0])
    queue = [root]
    for node in queue:
        for side in ("left", "right"):
            v = next(it, None)
            if v is not None:
                child = TreeNode(v)
                setattr(node, side, child)
                queue.append(child)
    return root


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


@pytest.mark.parametrize("values, expected", [
    ([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
     [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]),
    ([0, None, 1], [1, None, 1]),
    ([5], [5]),
    ([], []),
])
def test_prob05(values, expected):
    assert to_level_list(prob05(build(values))) == expected
