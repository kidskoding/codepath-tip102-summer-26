# Problem Set: Recursion — Interview Practice

---

## Problem 1: Flatten a Nested List

**Difficulty:** Medium

### Description

Given a list that may contain integers or other lists (nested to any depth), return a single flat list of all the integers in left-to-right order.

**A solution is considered valid if:**
- It handles arbitrary nesting depth
- It preserves the original left-to-right order of elements
- It uses recursion to descend into nested lists

### Function Signature

```python
def flatten(nested: list) -> list:
    pass
```

### Examples

**Example 1:**
```
Input:  [1, [2, 3], [4, [5, 6]]]
Output: [1, 2, 3, 4, 5, 6]
```

**Example 2:**
```
Input:  [[1, [2]], 3]
Output: [1, 2, 3]
```

**Example 3:**
```
Input:  []
Output: []
```

---

## Problem 2: Power of a Number

**Difficulty:** Medium

### Description

Implement `pow(x, n)`, which raises `x` to the integer power `n`, without using the built-in `**` operator or `math.pow`. Support negative exponents.

**A solution is considered valid if:**
- It handles `n == 0` (returns 1)
- It handles negative `n` (returns 1 / x^|n|)
- Bonus: runs in O(log n) using fast exponentiation

### Function Signature

```python
def my_pow(x: float, n: int) -> float:
    pass
```

### Examples

**Example 1:**
```
Input:  x = 2, n = 10
Output: 1024.0
```

**Example 2:**
```
Input:  x = 2, n = -2
Output: 0.25
```

**Example 3:**
```
Input:  x = 5, n = 0
Output: 1.0
```

---

## Problem 3: Binary Search Recursively

**Difficulty:** Easy

### Description

Given a sorted list of integers `nums` and a `target`, return the index of `target` if it is present, otherwise return `-1`. Implement the search recursively.

**A solution is considered valid if:**
- It uses recursion (not a loop)
- It runs in O(log n) time
- It returns `-1` when the target is absent

### Function Signature

```python
def binary_search(nums: list, target: int) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  nums = [1, 3, 5, 7, 9], target = 7
Output: 3
```

**Example 2:**
```
Input:  nums = [1, 3, 5, 7, 9], target = 4
Output: -1
```

---

## Problem 4: Generate All Permutations of a String

**Difficulty:** Medium

### Description

Given a string `s`, return a list of all its permutations. You may return the permutations in any order. Assume the characters are distinct.

**A solution is considered valid if:**
- It returns all `n!` permutations for a string of length `n`
- It uses recursion / backtracking

### Function Signature

```python
def permutations(s: str) -> list:
    pass
```

### Examples

**Example 1:**
```
Input:  "abc"
Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
```

**Example 2:**
```
Input:  "a"
Output: ["a"]
```

---

## Problem 5: Generate All Subsets of a Set

**Difficulty:** Medium

### Description

Given a list of distinct integers `nums`, return all possible subsets (the power set). The solution set must not contain duplicate subsets; return them in any order.

**A solution is considered valid if:**
- It returns all `2^n` subsets, including the empty set and the full set
- It uses recursion / backtracking

### Function Signature

```python
def subsets(nums: list) -> list:
    pass
```

### Examples

**Example 1:**
```
Input:  [1, 2, 3]
Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

**Example 2:**
```
Input:  []
Output: [[]]
```

---

## Problem 6: Validate a BST Recursively

**Difficulty:** Medium

### Description

Given the `root` of a binary tree, determine whether it is a valid binary search tree (BST). A valid BST requires that every node's value is greater than all values in its left subtree and less than all values in its right subtree.

**A solution is considered valid if:**
- It returns `True` only for a valid BST
- It correctly rejects trees where a deep descendant violates the ordering (not just direct children)
- It uses recursion with min/max bounds

### Function Signature

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    pass
```

### Examples

**Example 1:**
```
Input:      2
           / \
          1   3
Output: True
```

**Example 2:**
```
Input:      5
           / \
          1   4
             / \
            3   6
Output: False   (4's left subtree contains 3, but 3 < 5 is violated on the right side)
```

---

## Problem 7: Path Sum in a Binary Tree

**Difficulty:** Easy

### Description

Given the `root` of a binary tree and an integer `target`, return `True` if the tree has a root-to-leaf path such that the sum of the node values along the path equals `target`.

**A solution is considered valid if:**
- The path must start at the root and end at a leaf (a node with no children)
- It uses recursion, subtracting each node's value as it descends

### Function Signature

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def has_path_sum(root: TreeNode, target: int) -> bool:
    pass
```

### Examples

**Example 1:**
```
Input:      5
           / \
          4   8
         /
        11
       /  \
      7    2
      target = 27   (5 -> 4 -> 11 -> 7)
Output: True
```

**Example 2:**
```
Input:  root = None, target = 0
Output: False
```

---

## Problem 8: Merge Sort / Quicksort Implementation

**Difficulty:** Medium

### Description

Implement a sorting algorithm from scratch using recursion. Choose **merge sort** or **quicksort** (or implement both). Return a new sorted list in ascending order — do not use Python's built-in `sorted()` or `list.sort()`.

**A solution is considered valid if:**
- It correctly sorts any list of comparable elements
- It uses the divide-and-conquer recursive structure of the chosen algorithm
- Merge sort: O(n log n) time. Quicksort: O(n log n) average, O(n^2) worst case

### Function Signature

```python
def merge_sort(nums: list) -> list:
    pass

def quicksort(nums: list) -> list:
    pass
```

### Examples

**Example 1:**
```
Input:  [5, 2, 9, 1, 5, 6]
Output: [1, 2, 5, 5, 6, 9]
```

**Example 2:**
```
Input:  []
Output: []
```

---
