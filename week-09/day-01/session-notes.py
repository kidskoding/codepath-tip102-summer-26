from collections import deque
from references import TreeNode

def in_order(root: TreeNode | None):
    if not root:
        return []
    
    return in_order(root.left) + [root.val] + in_order(root.right)

def level_order(root: TreeNode | None) -> list[TreeNode]:
    if root is None:
        return []

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
