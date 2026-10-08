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

FLAVORS1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot",
            None, None, None, None, "Chai", "Maple", None, "Smore"]
FLAVORS2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]


@pytest.mark.parametrize("a, b, expected", [
    (FLAVORS1, FLAVORS2, True),
    (["Red Velvet", "Vanilla", "Lemon"], ["Red Velvet", "Lemon", "Vanilla"], True),
    (["Red Velvet", "Vanilla", "Lemon"], ["Red Velvet", "Vanilla", "Ube"], False),  # different flavor
    (["Red Velvet", "Vanilla"], ["Red Velvet", "Vanilla", "Lemon"], False),  # different size
    ([], [], True),
])
def test_prob04(a, b, expected):
    assert prob04(build(a), build(b)) == expected
