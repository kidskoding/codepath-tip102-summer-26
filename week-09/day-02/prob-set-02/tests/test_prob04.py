import pytest
from references import TreeNode
from prob04 import prob04


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
    (["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"], 3),
    (["👻", "👻", "👻"], 1),
    (["👻", "🧛🏾", "🧛🏾"], 3),  # same theme but not connected to each other
    (["👻"], 1),
    ([], 0),
])
def test_prob04(values, expected):
    assert prob04(build(values)) == expected
