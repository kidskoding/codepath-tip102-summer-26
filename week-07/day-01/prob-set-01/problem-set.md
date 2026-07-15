# Problem Set: Recursion — Week 7, Day 1 (Version 1)

---

## Problem 1: Counting Iron Man's Suits

**Difficulty:** Easy

### Description

Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings `suits` where each string is a suit in Stark's collection, count the total number of suits in the list. Implement it both iteratively and recursively — without using `len()`.

### Function Signature

```python
def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
```

### Examples

**Example 1:**
```
Input:  ["Mark I", "Mark II", "Mark III"]
Output: 3
```

---

## Problem 2: Collecting Infinity Stones

**Difficulty:** Easy

### Description

Thanos is collecting Infinity Stones. Given an array of integers `stones` representing the power of each stone, return the total power using a recursive approach.

### Function Signature

```python
def prob02(stones):
    pass
```

### Examples

**Example 1:**
```
Input:  [5, 10, 15, 20, 25, 30]
Output: 105
```

**Example 2:**
```
Input:  [12, 8, 22, 16, 10]
Output: 68
```

---

## Problem 3: Counting Iron Man's Unique Suits

**Difficulty:** Medium

### Description

Some of Iron Man's suits are duplicates. Given a list of strings `suits` where each string is a suit in Stark's collection, count the total number of **distinct** suits in the list. Implement it both iteratively and recursively.

### Function Signature

```python
def count_suits_iterative(suits):
    pass

def count_suits_recursive(suits):
    pass
```

### Examples

**Example 1:**
```
Input:  ["Mark I", "Mark I", "Mark III"]
Output: 2
```

---

## Problem 4: Calculating Groot's Growth

**Difficulty:** Medium

### Description

Groot grows according to the Fibonacci sequence. Given `n`, find the height of Groot after `n` months using recursion.

The Fibonacci numbers `F(n)` form a sequence where each number is the sum of the two preceding ones, starting from 0 and 1:
- `F(0) = 0`, `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)`, for `n > 1`.

### Function Signature

```python
def prob04(n):
    pass
```

### Examples

**Example 1:**
```
Input:  5
Output: 5
```

**Example 2:**
```
Input:  8
Output: 21
```

---

## Problem 5: Calculating the Power of the Fantastic Four

**Difficulty:** Medium

### Description

The Fantastic Four's power level is represented as a power of 4. Write a recursive function that calculates 4 raised to the `n`th power. Support negative exponents.

### Function Signature

```python
def prob05(n):
    pass
```

### Examples

**Example 1:**
```
Input:  2
Output: 16
```
Explanation: 4 to the 2nd power (4 * 4) is 16.

**Example 2:**
```
Input:  -2
Output: 0.0625
```
Explanation: 4 to the power of -2 is 1 / (4 * 4) = 0.0625.

---

## Problem 6: Strongest Avenger

**Difficulty:** Easy

### Description

Given a list of the Avengers' `strengths`, find the maximum strength using a recursive approach — without using `max()`.

### Function Signature

```python
def prob06(strengths):
    pass
```

### Examples

**Example 1:**
```
Input:  [88, 92, 95, 99, 97, 100, 94]
Output: 100
```

**Example 2:**
```
Input:  [50, 75, 85, 60, 90]
Output: 90
```

---

## Problem 7: Counting Vibranium Deposits

**Difficulty:** Medium

### Description

In Wakanda, vibranium deposits are represented by characters in a string (e.g. `"V"` for vibranium, `"G"` for gold). Given a string `resources`, write a recursive function `prob07()` that returns the total number of vibranium (`"V"`) deposits in `resources`.

### Function Signature

```python
def prob07(resources):
    pass
```

### Examples

**Example 1:**
```
Input:  "VVVVV"
Output: 5
```

**Example 2:**
```
Input:  "VXVYGA"
Output: 2
```
Explanation: There are two `"V"` characters in `"VXVYGA"`.

---

## Problem 8: Merging Missions

**Difficulty:** Medium

### Description

Each Avengers mission has a priority level represented as a node in a sorted linked list. Given the heads of two sorted linked lists `mission1` and `mission2`, implement a **recursive** function `prob08()` that merges them into one sorted list by splicing together the existing nodes. Return the head of the merged list.

### Function Signature

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def prob08(mission1, mission2):
    pass
```

### Examples

**Example 1:**
```
Input:  mission1: 1 -> 2 -> 4
        mission2: 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

---

## Problem 9: Merging Missions II (SKIPPED)

_Discussion/comparison problem — no implementation._

Compare your recursive `prob08()` from Problem 8 to the iterative solution provided in the source, and discuss which you prefer.

---
