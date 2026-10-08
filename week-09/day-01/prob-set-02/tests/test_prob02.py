import pytest
from references import TreeNode
from prob02 import prob02


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


def test_prob02_example():
    hotel = TreeNode("Lobby",
                     TreeNode(101, TreeNode(201, TreeNode(301)), TreeNode(202)),
                     TreeNode(102, TreeNode(203), TreeNode(204, None, TreeNode(302))))
    assert prob02(hotel) == ["Lobby", 101, 102, 201, 202, 203, 204, 301, 302]


@pytest.mark.parametrize("values, expected", [
    ([], []),
    (["Lobby"], ["Lobby"]),
    (["Lobby", None, 102, 203], ["Lobby", 102, 203]),
])
def test_prob02(values, expected):
    assert prob02(build(values)) == expected
