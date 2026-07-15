# Problem Set: Binary Search & Divide and Conquer — Week 7, Day 2

---

## Problem 1: Finding the Perfect Cruise

**Difficulty:** Easy

### Description

It's vacation time! Given an integer `vacation_length` and a list of integers `cruise_lengths` sorted in ascending order, use binary search to return `True` if there is a cruise length that matches `vacation_length`, and `False` otherwise.

### Function Signature

```python
def find_cruise_length(cruise_lengths, vacation_length):
    pass
```

### Examples

**Example 1:**
```
Input:  [9, 10, 11, 12, 13, 14, 15], 13
Output: True
```

**Example 2:**
```
Input:  [8, 9, 12, 13, 13, 14, 15], 11
Output: False
```

---

## Problem 2: Booking the Perfect Cruise Cabin

**Difficulty:** Medium

### Description

You have a list of available `cabins` sorted in ascending order by deck level. Given `cabins` and an integer `preferred_deck`, write a **recursive** function `find_cabin_index()` that returns the index of `preferred_deck`. If a cabin with `preferred_deck` does not exist, return the index where it would be inserted to keep `cabins` sorted.

Your algorithm must run in O(log n) time.

### Function Signature

```python
def find_cabin_index(cabins, preferred_deck):
    pass
```

### Examples

**Example 1:**
```
Input:  [1, 3, 5, 6], 5
Output: 2
```

**Example 2:**
```
Input:  [1, 3, 5, 6], 2
Output: 1
```

**Example 3:**
```
Input:  [1, 3, 5, 6], 7
Output: 4
```

---

## Problem 3: Count Checked In Passengers

**Difficulty:** Medium

### Description

You are given a list of `rooms` where passengers are either checked in (`1`) or not checked in (`0`). The list is sorted, so all the `0`s appear before any `1`s. Write a function `count_checked_in_passengers()` that counts and returns the total number of checked-in passengers (`1`s) in O(log n) time.

### Function Signature

```python
def count_checked_in_passengers(rooms):
    pass
```

### Examples

**Example 1:**
```
Input:  [0, 0, 0, 1, 1, 1, 1]
Output: 4
```

**Example 2:**
```
Input:  [0, 0, 0, 0, 0, 1]
Output: 1
```

**Example 3:**
```
Input:  [0, 0, 0, 0, 0, 0]
Output: 0
```

---

## Problem 4: Determining Profitability of Excursions

**Difficulty:** Medium

### Description

You have a sorted list of non-negative integers `excursion_counts`, where each number represents how many passengers signed up for various excursions. The list is **profitable** if there exists a number `x` such that there are exactly `x` excursions with **at least** `x` passengers signed up.

Return the value of `x` if `excursion_counts` is profitable, otherwise return `-1`. If profitable, `x` is unique.

### Function Signature

```python
def is_profitable(excursion_counts):
    pass
```

### Examples

**Example 1:**
```
Input:  [3, 5]
Output: 2
```
Explanation: There are 2 values (3 and 5) that are `>= 2`.

**Example 2:**
```
Input:  [0, 0]
Output: -1
```
Explanation: No `x` fits — for `x = 1` there should be 1 number `>= 1`, but there are 0; and so on.

---

## Problem 5: Finding the Shallowest Point

**Difficulty:** Medium

### Description

Given an array of integers `depths` representing water depths along a route, write a function `find_shallowest_point()` that uses a **divide-and-conquer** approach to return the shallowest point (minimum value) in `depths`. You may not use the built-in `min()` function.

### Function Signature

```python
def find_shallowest_point(depths):
    pass
```

### Examples

**Example 1:**
```
Input:  [5, 7, 2, 8, 3]
Output: 2
```

**Example 2:**
```
Input:  [12, 15, 10, 21]
Output: 10
```

---

## Problem 6: Cruise Ship Treasure Hunt

**Difficulty:** Medium

### Description

A chest of candy is hidden in one of the rooms on board. The rooms are organized in an `m x n` grid `matrix`, where each row and each column are sorted in ascending order by room number. Given an integer `treasure` (the room number where the prize is hidden), use a **divide-and-conquer** approach to return a tuple `(row, col)` of the indices where `treasure` is found. If `treasure` is not in `matrix`, return `(-1, -1)`.

### Function Signature

```python
def find_treasure(matrix, treasure):
    pass
```

### Examples

**Example 1:**
```
Input:  matrix = [
            [1, 4, 7, 11],
            [8, 9, 10, 20],
            [11, 12, 17, 30],
            [18, 21, 23, 40]
        ], treasure = 17
Output: (2, 2)
```

**Example 2:**
```
Input:  (same matrix), treasure = 5
Output: (-1, -1)
```

---
