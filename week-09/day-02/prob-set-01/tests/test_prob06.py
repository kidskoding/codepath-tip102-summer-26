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


def bakery():
    cupcakes, macaron, cookies = TreeNode("Cupcakes"), TreeNode("Macaron"), TreeNode("Cookies")
    cake, eclair, croissant = TreeNode("Cake"), TreeNode("Eclair"), TreeNode("Croissant")
    cupcakes.left, cupcakes.right = macaron, cookies
    macaron.right = cake
    cookies.left, cookies.right = eclair, croissant
    return dict(cupcakes=cupcakes, macaron=macaron, cookies=cookies, cake=cake, eclair=eclair, croissant=croissant)


@pytest.mark.parametrize("current, expected", [
    ("cake", "eclair"),  # crosses to a different parent
    ("cookies", None),  # rightmost on its level
    ("macaron", "cookies"),
    ("eclair", "croissant"),
    ("cupcakes", None),  # root is alone on its level
])
def test_prob06(current, expected):
    t = bakery()
    result = prob06(t["cupcakes"], t[current])
    if expected is None:
        assert result is None
    else:
        assert result is t[expected]
