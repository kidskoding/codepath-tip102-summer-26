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
    (["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"],
     ["Chocolate", "Lemon", "Vanilla", "Strawberry", "Hazelnut", "Red Velvet"]),
    ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 4, 5, 6, 7]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
     [1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8]),  # 4th row right to left again
    ([], []),
])
def test_prob06(values, expected):
    assert prob06(build(values)) == expected
