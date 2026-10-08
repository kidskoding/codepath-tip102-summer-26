# Problem Set: Binary Search & Divide and Conquer (Music) — Week 7, Day 2

---

## Problem 1: Finding the Perfect Song

### Description

Abby Lee of Dance Moms needs a song of a specific length for a group routine. Given a list `playlist` of song lengths sorted in ascending order and a target `length`, write a function `prob01()` that uses binary search to return the index of the song with that length, or `-1` if there is none.

### Function Signature

```python
def prob01(playlist, length):
    pass
```

### Examples

**Example 1:**
```
Input:  playlist = [101, 102, 103, 104, 105], length = 103
Output: 2
```

**Example 2:**
```
Input:  playlist = [201, 202, 203, 204, 205], length = 206
Output: -1
```

---

## Problem 2: Finding Tour Dates

### Description

Your favorite artist has a short residency in your city, but you're only free one day this month. Given a sorted list of integers `tour_dates` (the days the artist plays) and an integer `available` (the day you're free), write a **recursive** function `prob02()` that returns `True` if some date in `tour_dates` matches `available`, and `False` otherwise.

Your solution must run in O(log n) time.

### Function Signature

```python
def prob02(tour_dates, available):
    pass
```

### Examples

**Example 1:**
```
Input:  tour_dates = [1, 3, 7, 10, 12], available = 12
Output: True
```

**Example 2:**
```
Input:  tour_dates = [1, 3, 7, 10, 12], available = 5
Output: False
```

---

## Problem 3: Sqrt(x)

### Description

Given a non-negative integer `x`, write a function `prob03()` that uses binary search to return the square root of `x` rounded down to the nearest integer.

You may not use any built-in exponent function or operator (e.g. `pow(x, 0.5)` or `x ** 0.5`), or external libraries like `math`.

Evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

### Function Signature

```python
def prob03(x):
    pass
```

### Examples

**Example 1:**
```
Input:  x = 4
Output: 2
```

**Example 2:**
```
Input:  x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., which rounds down to 2.
```

---

## Problem 4: Granting Backstage Access

### Description

The artist can meet two groups of fans backstage before the show. Given a list `group_sizes`, where each element is the size of a group of friends, and an integer `room_capacity`, write a function `prob04()` that uses binary search to return the largest sum of two distinct groups that is **strictly less than** `room_capacity`. If no such pair exists, return `-1`.

Evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

### Function Signature

```python
def prob04(group_sizes, room_capacity):
    pass
```

### Examples

**Example 1:**
```
Input:  group_sizes = [1, 20, 10, 14, 3, 5, 4, 2], room_capacity = 12
Output: 11
Explanation: 1 + 10 = 11, which is less than 12.
```

**Example 2:**
```
Input:  group_sizes = [10, 20, 30], room_capacity = 15
Output: -1
Explanation: No pair sums to less than 15.
```

---

## Problem 5: Harmonizing Two Musical Tracks

### Description

You have two tracks, `track1` and `track2`, each a sorted list of pitch values. Write a function `prob05()` that uses a divide-and-conquer approach to merge them into a single sorted list and return it.

Evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

### Function Signature

```python
def prob05(track1, track2):
    pass
```

### Examples

**Example 1:**
```
Input:  track1 = [1, 3, 5], track2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
```

**Example 2:**
```
Input:  track1 = [10, 20], track2 = [15, 30]
Output: [10, 15, 20, 30]
```

---

## Problem 6: Merge Sort Playlist

### Description

Given a list of strings `playlist`, use merge sort to write a recursive function `merge_sort_playlist()` that returns the songs sorted in alphabetical order. It uses a helper, `merge_sort_helper()`, that merges two sorted lists.

This problem has two functions, so both keep their given names (not `prob06`). The pseudocode is in `prob06.py`:

```python
def merge_sort_helper(left_arr, right_arr):
    # Create an empty list to store merged result list
    # Use pointers to iterate through left_arr and right_arr
        # Compare their elements, and add the smaller element to result list
        # Increment pointer of list with smaller element
    # Add any remaining elements from the left half
    # Add any remaining elements from the right half
    # Return the merged list
    pass

def merge_sort_playlist(playlist):
    # Base Case:
    # If the list has 1 or 0 elements, it's already sorted

    # Recursive Cases:
    # Divide the list into two halves
    # Merge sort first half
    # Merge sort second half
    # Use the helper to merge the sorted halves (pass in sorted left half, and sorted right half)
    # Return the merged list
    pass
```

### Function Signature

```python
def merge_sort_helper(left_arr, right_arr):
    pass

def merge_sort_playlist(playlist):
    pass
```

### Examples

**Example 1:**
```
Input:  playlist = ["Formation", "Crazy in Love", "Halo"]
Output: ['Crazy in Love', 'Formation', 'Halo']
```

**Example 2:**
```
Input:  playlist = ["Single Ladies", "Love on Top", "Irreplaceable"]
Output: ['Irreplaceable', 'Love on Top', 'Single Ladies']
```

---
