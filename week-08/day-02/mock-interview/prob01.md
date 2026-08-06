# Mock Interview: Kth Smallest Element in a BST — Week 8

**Difficulty:** Medium

### Description

Given the `root` of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

### Function Signature

```python
def prob01(root, k: int) -> int:
    pass
```

### Examples

**Example 1:**
```
    3
   / \
  1   4
   \
    2

Input:  root = [3, 1, 4, null, 2], k = 1
Output: 1
```

**Example 2:**
```
        5
       / \
      3   6
     / \
    2   4
   /
  1

Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
Output: 3
```

### Constraints

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

**Follow up:** If the BST is modified often (insert/delete) and you need to find the kth smallest frequently, how would you optimize?
