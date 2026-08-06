from collections import deque

from references.treenode import TreeNode

def prob01(root: TreeNode | None) -> list:
    res = []
    if not root:
        return res

    goes_left = False
    queue = deque([root])
    while queue:
        curr_level = deque()
        n = len(queue)

        for _ in range(n):
            node = queue.popleft()

            if goes_left:
                curr_level.append(node.val)
            else:
                curr_level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(curr_level)
        goes_left = not goes_left

    return res
