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


def build_kv(pairs):
    """level-order list of (key, val) tuples (None = no node) -> tree"""
    if not pairs:
        return None
    it = iter(pairs[1:])
    root = TreeNode(pairs[0][1], key=pairs[0][0])
    queue = [root]
    for node in queue:
        for side in ("left", "right"):
            p = next(it, None)
            if p is not None:
                child = TreeNode(p[1], key=p[0])
                setattr(node, side, child)
                queue.append(child)
    return root


HOTEL1 = [(3, "Lobby"), (1, 101), (4, 102), None, (2, 201)]
HOTEL2 = [(5, "Lobby"), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]


@pytest.mark.parametrize("pairs, k, expected", [
    (HOTEL1, 1, 101),
    (HOTEL2, 3, 101),
    (HOTEL2, 1, 301),
    (HOTEL2, 6, 102),  # k = n: least spooky
    ([(1, "Lobby")], 1, "Lobby"),
])
def test_prob06(pairs, k, expected):
    assert prob06(build_kv(pairs), k) == expected
