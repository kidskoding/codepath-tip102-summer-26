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

BAKED = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]


@pytest.mark.parametrize("values, order_size, expected", [
    (BAKED, 22, True),  # 5 + 4 + 11 + 2
    (BAKED, 2, False),
    (BAKED, 26, True),  # 5 + 8 + 13
    (BAKED, 9, False),  # 5 + 4 is not a root-to-leaf path
    ([], 0, False),
    ([1, 2], 1, False),  # the root alone is not a leaf here
])
def test_prob05(values, order_size, expected):
    assert prob05(build(values), order_size) == expected
