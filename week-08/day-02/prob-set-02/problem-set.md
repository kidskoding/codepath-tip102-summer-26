# Problem Set #2: Binary Search Trees — Week 8, Day 2

All problems use the shared `TreeNode` class (the source's `Cichlid`/`Pearl`
classes have the identical shape — attribute is `.val`):

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
```

---

## Problem 1: Find Lonely Cichlids

**Difficulty:** Easy

### Description

Sibling cichlid fish often form strong bonds after hatching, staying close to each other for protection. Given the root of a binary tree representing a family of cichlids where each node is a cichlid, return an array containing the values of all lonely cichlids in the family. A lonely cichlid is a fish (node) that is the only child of its parent. The matriarch (root) is not lonely because it does not have a parent. Return the array in any order.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob01(root):
    pass
```

### Examples

**Example 1:**
```
    A
   / \
  B   C
   \
    D

Input:  root of the tree above
Output: ['D']
```

**Example 2:**
```
     A
    / \
   B   C
  /   / \
 D   E   F
          \
           G

Input:  root of the tree above
Output: ['D', 'G']
```

**Example 3:**
```
                 A
                / \
               B   C
              /     \
             D       E
            /         \
           F           G
          /             \
         H               I

Input:  root of the tree above
Output: ['D', 'F', 'H', 'E', 'G', 'I']
```

Note: The elements of the list may be returned in any order.

---

## Problem 2: Searching Ariel's Treasures

**Difficulty:** Easy

### Description

The mermaid princess Ariel is looking for a specific item in the grotto where she collects objects from the human world. Ariel's collection is stored in a binary search tree (BST) where each node represents a different item in her collection. The items are organized according to their names (`val`) in alphabetical order in the BST.

Given the root of the binary search tree `grotto` and a target object `treasure`, return `True` if `treasure` is present in the collection and `False` otherwise.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob02(grotto, treasure):
    pass
```

### Examples

**Example 1:**
```
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit

Input:  grotto = root of the tree above, treasure = "Dinglehopper"
Output: True
```

**Example 2:**
```
Input:  grotto = same tree, treasure = "Thingamabob"
Output: False
```

---

## Problem 3: Add New Treasure to Collection

**Difficulty:** Medium

### Description

Ariel and her pal Flounder visited a new shipwreck and found an exciting new human artifact to add to her collection, stored in a BST organized alphabetically by item name (`val`).

Given the root of the binary search tree `grotto` and a string `new_item`, add a new node with value `new_item` to the collection and return the root of the modified tree. If a node with value `new_item` already exists within the tree, return the original tree unmodified. You do not need to maintain balance in the tree.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob03(grotto, new_item):
    pass
```

### Examples

**Example 1:**
```
             Snarfblat
            /        \
        Gadget       Whatzit
       /     \           \
Dinglehopper Gizmo       Whozit

Input:  grotto = root of the tree above, new_item = "Thingamabob"
Output: root of the updated tree:

               Snarfblat
            /             \
        Gadget            Whatzit
       /     \           /       \
Dinglehopper Gizmo  Thingamabob  Whozit
```

---

## Problem 4: Sorting Pearls by Size

**Difficulty:** Medium

### Description

You have a collection of pearls organized by size in a BST, where each node represents the size of a pearl. A recursive `smallest_to_largest_recursive()` has been provided. Implement an **iterative** version that takes in the BST root `pearls` and returns an array of pearl sizes sorted from smallest to largest.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Starter Code

```python
def smallest_to_largest_recursive(pearls):
    sorted_list = []

    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            sorted_list.append(node.val)
            inorder_traversal(node.right)

    inorder_traversal(pearls)
    return sorted_list
```

### Function Signature

```python
def prob04(pearls):
    pass
```

### Examples

**Example 1:**
```
        3
       / \
      /   \
     1     5
      \   / \
       2 4   8

Input:  pearls = root of the tree above
Output: [1, 2, 3, 4, 5, 8]
```

---

## Problem 5: Smallest Pearl Above Minimum Size

**Difficulty:** Medium

### Description

You have a collection of pearls stored in a BST where each node represents a pearl with size `val`. You are looking for a pearl to gift the sea goddess Yemaya — the pearl must be larger than `min_size`.

Given the root of a BST `pearls`, return the size of the pearl with the smallest size above `min_size`. If no pearl with a size above `min_size` exists, return `None`.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob05(pearls, min_size):
    pass
```

### Examples

**Example 1:**
```
        3
       / \
      /   \
     1     5
      \   / \
       2 4   8

Input:  pearls = root of the tree above, min_size = 3
Output: 4
```

**Example 2:**
```
Input:  pearls = same tree, min_size = 7
Output: 8
```

**Example 3:**
```
Input:  pearls = same tree, min_size = 8
Output: None
```

---

## Problem 6: Remove Invasive Species

**Difficulty:** Hard

### Description

As a marine ecologist, you are worried about invasive species wreaking havoc on the local ecosystem. Given the root of a BST `ecosystem` where each node represents a species, and an invasive species `name`, remove the node with value `name` from the ecosystem. Return the root of the modified ecosystem. Species are organized alphabetically in the tree by `val`.

If the node with `name` has two children in the tree, replace it with its inorder successor (leftmost node in its right subtree). You do not need to maintain a balanced tree.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob06(ecosystem, name):
    # Find the node to remove
    # If the node has no children
        # Remove the node by setting parent pointer to None
    # If the node has one child
        # Replace the node with its child
    # If the node has two children
        # Find the inorder successor
        # Replace the node's value with inorder successor value
        # Remove inorder successor
    # Return root of updated tree
    pass
```

### Examples

**Example 1:**
```
                Dugong
             /         \
       Brain Coral   Lionfish
              \       /       \
         Clownfish Giant Clam  Seagrass

Input:  ecosystem = root of the tree above, name = "Lionfish"
Output: root of the updated tree:

             Dugong
            /      \
      Brain Coral  Seagrass
            \         /
        Clownfish  Giant Clam
```

---

## Problem 7: Minimum Difference in Pearl Size

**Difficulty:** Medium

### Description

You are analyzing your collection of pearls stored in a BST where each node represents a pearl with a specific size (`val`). You want to see if you have two pearls of similar size that you can make into a pair of earrings.

Given the root of a BST `pearls`, return the minimum difference between the sizes of any two different pearls in the collection.

Evaluate the time complexity of your function. Assume the input tree is balanced.

### Function Signature

```python
def prob07(pearls):
    pass
```

### Examples

**Example 1:**
```
        4
       / \
      2   6
     / \   \
    1   3   8

Input:  pearls = root of the tree above
Output: 1
```
The difference between pearl sizes 3 and 4, or 2 and 3.

---
