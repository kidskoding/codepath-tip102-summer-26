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
    (["👻", "😱", "🧛🏾‍♀️", "💀", "😈"], [["💀", "😈", "🧛🏾‍♀️"], ["😱"], ["👻"]]),
    (["👻"], [["👻"]]),
    ([1, 2, None, 3], [[3], [2], [1]]),  # chain
    ([], []),
])
def test_prob05(values, expected):
    result = prob05(build(values))
    # leaves inside one round may come back in any order
    assert [sorted(r) for r in result] == [sorted(r) for r in expected]
