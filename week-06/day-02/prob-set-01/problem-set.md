# Problem Set #1: Linked Lists — Week 6, Day 2

---

## Problem 1: Wild Goose Chase

**Difficulty:** Easy

### Description

You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy — you suspect the clue might be a red herring meant to send you around in circles.

Write a function `prob01()` that accepts the head of a singly linked list `clues` and returns `True` if the tail of the linked list points at the head of the linked list. Otherwise, return `False`.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob01(clues):
    pass
```

### Examples

**Example 1:**
```
Input:  Circular linked list of 3 clues where the 3rd clue points to the 1st clue
        clue1 -> clue2 -> clue3 -> clue1
Output: True
```

---

## Problem 2: Breaking the Cycle

**Difficulty:** Medium

### Description

All the clues that lead us in circles are false evidence we need to purge! Given the head of a linked list `evidence`, clean up the evidence list by identifying any false clues.

Write a function `prob02()` that returns an array containing all values that are part of any cycle in `evidence`. Return the values in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob02(evidence):
    pass
```

### Examples

**Example 1:**
```
Input:  Linked list with 4 clues where the 4th clue points to the 2nd clue
        clue1 -> clue2 -> clue3 -> clue4 -> clue2
Output: ['The stolen goods are at an abandoned warehouse',
         'The mayor is accepting bribes',
         'They dumped their disguise in the lake']
```

**Example 2:**
```
Input:  Linked list with no cycle
        clue5 -> clue6 -> clue7
Output: []
```

---

## Problem 3: Prioritizing Suspects

**Difficulty:** Medium

### Description

You've identified a list of suspects, but time is limited and you won't be able to question all of them today.

Write a function `prob03()` to help prioritize the order in which you question suspects. Given the head of a linked list of integers `suspect_ratings`, where each integer represents the suspiciousness of a given suspect, and a value `threshold`, prob03 the linked list such that all nodes with values greater than `threshold` come before nodes with values less than or equal to `threshold`.

Return the head of the partitioned list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

**A solution is considered valid if:**
- All nodes with value > `threshold` appear before all nodes with value <= `threshold`
- The relative order within each group may be anything

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob03(suspect_ratings, threshold):
    pass
```

### Examples

**Example 1:**
```
Input:  1 -> 4 -> 3 -> 2 -> 5 -> 2, threshold = 3
Output: 4 -> 5 -> 1 -> 3 -> 2 -> 2
```

Note that nodes 4 and 5 can be in any order so long as they come before 3, 2, and 1. Similarly, 3, 2, and 1 can come in any order so long as they are after 4 and 5. `5 -> 4 -> 3 -> 1 -> 2 -> 2` would also be acceptable.

---

## Problem 4: Puzzling it Out

**Difficulty:** Easy

### Description

A new witness has emerged and provided a new account of events the night of the crime. Given the heads of two sorted linked lists, `known_timeline` and `witness_timeline`, each representing a numbered sequence of events, merge the two timelines into one sorted sequence of events.

The resulting linked list should be made by splicing together the nodes of the first two timelines. Return the head of the merged timeline.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob04(known_timeline, witness_timeline):
    pass
```

### Examples

**Example 1:**
```
Input:  known_timeline:   1 -> 2 -> 4
        witness_timeline: 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

---

## Problem 5: A New Perspective

**Difficulty:** Medium

### Description

You're having a tough time making a break in the case, and it's time to shake things up to gain a new perspective. Given the head of a linked list of numbered pieces of evidence `evidence`, and a non-negative integer `k`, rotate the list to the right by `k` places.

Return the head of the rotated list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob05(evidence, k):
    pass
```

### Examples

**Example 1:**
```
Input:  1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 4 -> 5 -> 1 -> 2 -> 3
```

**Example 2:**
```
Input:  0 -> 1 -> 2, k = 4
Output: 2 -> 0 -> 1
```

---

## Problem 6: Adding Up the Evidence

**Difficulty:** Medium

### Description

You have all your evidence, and it's time to sum it to the final answer! You are given the heads of two non-empty linked lists `head_a` and `head_b` representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list. The digits of the sum should also be stored in reverse order, with each node containing a single digit.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob06(head_a, head_b):
    pass
```

### Examples

**Example 1:**
```
Input:  head_a: 2 -> 4 -> 3   (represents 342)
        head_b: 5 -> 6 -> 4   (represents 465)
Output: 7 -> 0 -> 8           (represents 807)
```
Explanation: 342 + 465 = 807
