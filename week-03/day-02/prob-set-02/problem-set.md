# Problem Set: Stacks, Queues & Two Pointers (Expedition) — Week 3, Day 2

---

## Problem 1: Final Costs After a Supply Discount

### Description

You are managing the budget for a global expedition. The integer list `costs` holds supply costs, where `costs[i]` is the cost of the `i`th item.

There is a special discount: if you buy item `i`, you get a discount equal to `costs[j]`, where `j` is the minimum index such that `j > i` and `costs[j] <= costs[i]`. If no such `j` exists, there is no discount.

Write a function `prob01()` that returns a list `final_costs`, where `final_costs[i]` is the final price of item `i` after the discount.

### Function Signature

```python
def prob01(costs):
    pass
```

### Examples

**Example 1:**
```
Input:  costs = [8, 4, 6, 2, 3]
Output: [4, 2, 4, 2, 3]
```

**Example 2:**
```
Input:  costs = [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]
```

**Example 3:**
```
Input:  costs = [10, 1, 1, 6]
Output: [9, 0, 1, 6]
```

---

## Problem 2: Find First Symmetrical Landmark Name

### Description

You encounter a series of landmarks, each a string in the list `landmarks`. A landmark name is **symmetrical** if it reads the same forward and backward.

Write a function `prob02()` that returns the first symmetrical landmark name, or an empty string `""` if there is none.

### Function Signature

```python
def prob02(landmarks):
    pass
```

### Examples

**Example 1:**
```
Input:  landmarks = ["canyon", "forest", "rotor", "mountain"]
Output: "rotor"
```

**Example 2:**
```
Input:  landmarks = ["plateau", "valley", "cliff"]
Output: ""
```

---

## Problem 3: Terrain Elevation Match

### Description

You are mapping terrain elevations. You are given a string `terrain` of length `n`, where:

- `terrain[i] == 'I'` means the elevation at point `i` is lower than at point `i + 1` (`elevation[i] < elevation[i + 1]`).
- `terrain[i] == 'D'` means the elevation at point `i` is higher than at point `i + 1` (`elevation[i] > elevation[i + 1]`).

Write a function `prob03()` that reconstructs the elevation sequence: a list of the `n + 1` integers `0` to `n`, each used once, that matches `terrain`. If several sequences are valid, return any of them.

### Function Signature

```python
def prob03(terrain):
    pass
```

### Examples

**Example 1:**
```
Input:  terrain = "IDID"
Output: [0, 4, 1, 3, 2]
```

**Example 2:**
```
Input:  terrain = "III"
Output: [0, 1, 2, 3]
```

**Example 3:**
```
Input:  terrain = "DDI"
Output: [3, 2, 0, 1]
```

---

## Problem 4: Find the Expedition Log Concatenation Value

### Description

Your journal entries are a 0-indexed integer list `logs`. Concatenating two entries joins their digits; for example, concatenating 15 and 49 gives 1549.

The concatenation value starts at 0. Until no entries remain:

- If there are at least two entries, concatenate the first and last entries, add the result to the concatenation value, and remove both entries.
- If only one entry is left, add its value to the concatenation value and remove it.

Write a function `prob04()` that returns the final concatenation value.

### Function Signature

```python
def prob04(logs):
    pass
```

### Examples

**Example 1:**
```
Input:  logs = [7, 52, 2, 4]
Output: 596
Explanation: 74 + 522 = 596.
```

**Example 2:**
```
Input:  logs = [5, 14, 13, 8, 12]
Output: 673
Explanation: 512 + 148 + 13 = 673.
```

---

## Problem 5: Number of Explorers Unable to Gather Supplies

### Description

Explorers gather supplies from a stockpile with two resource types: type `0` (food rations) and type `1` (medical kits). The explorers stand in a queue, each preferring one type. There are as many supplies as explorers, stacked in a pile. At each step:

- If the explorer at the front of the queue prefers the resource on top of the stack, they take it and leave the queue.
- Otherwise, they leave the resource and go to the end of the queue.

This continues until no explorer in the queue wants the top resource.

You are given integer lists `explorers` and `supplies`. `supplies[i]` is the type of the `i`th resource in the stack (`i = 0` is the top). `explorers[j]` is the preference of the `j`th explorer in the queue (`j = 0` is the front). Write a function `prob05()` that returns the number of explorers unable to get their preferred supply.

### Function Signature

```python
def prob05(explorers, supplies):
    pass
```

### Examples

**Example 1:**
```
Input:  explorers = [1, 1, 0, 0], supplies = [0, 1, 0, 1]
Output: 0
```

**Example 2:**
```
Input:  explorers = [1, 1, 1, 0, 0, 1], supplies = [1, 0, 0, 0, 1, 1]
Output: 3
```

### Constraints

- `len(explorers) == len(supplies)`

---

## Problem 6: Count Balanced Terrain Subsections

### Description

You are analyzing a binary string `terrain`, where `0` is a valley and `1` is a hill. A **balanced subsection** is a non-empty contiguous segment with an equal number of `0`s and `1`s, where all the `0`s are grouped together and all the `1`s are grouped together.

Write a function `prob06()` that returns the total number of balanced subsections. Subsections that occur multiple times are counted each time.

### Function Signature

```python
def prob06(terrain):
    pass
```

### Examples

**Example 1:**
```
Input:  terrain = "00110011"
Output: 6
```

**Example 2:**
```
Input:  terrain = "10101"
Output: 4
```

---

## Problem 7: Check if a Signal Occurs as a Prefix in Any Transmission

### Description

A `transmission` consists of signals separated by single spaces. Write a function `prob07()` that returns the 1-indexed position of the first signal in `transmission` that has `searchSignal` as a prefix. If no signal does, return `-1`.

A prefix of a string `s` is any leading contiguous substring of `s`.

### Function Signature

```python
def prob07(transmission, searchSignal):
    pass
```

### Examples

**Example 1:**
```
Input:  transmission = "i love eating burger", searchSignal = "burg"
Output: 4
```

**Example 2:**
```
Input:  transmission = "this problem is an easy problem", searchSignal = "pro"
Output: 2
```

**Example 3:**
```
Input:  transmission = "i am tired", searchSignal = "you"
Output: -1
```

---
