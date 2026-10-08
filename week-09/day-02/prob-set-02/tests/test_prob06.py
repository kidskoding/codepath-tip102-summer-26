import pytest
from references import TreeNode
from prob06 import prob06


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
    (["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"], [202, "😱", "👻"]),
    (["Lobby", 101, 102, None, "💀"], ["💀"]),
    (["Lobby", 101, 102], ["Lobby", 101, 102]),  # both leaves deepest: whole tree
    (["Lobby"], ["Lobby"]),
])
def test_prob06(values, expected):
    assert to_level_list(prob06(build(values))) == expected
