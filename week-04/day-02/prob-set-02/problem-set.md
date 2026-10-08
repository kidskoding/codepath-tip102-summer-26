# Problem Set: Dictionaries & Hashing (Podcasts) — Week 4, Day 2

For every problem, also evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

---

## Problem 1: Track Podcast Episodes by Length

### Description

You manage a podcast and want to analyze episode lengths. Given a list `episode_lengths` of durations in minutes, write a function `prob01()` that counts how many episodes fall into each range: less than 30 minutes, 30 to 60 minutes, and more than 60 minutes. Return the three counts as a tuple in that order.

### Function Signature

```python
def prob01(episode_lengths):
    pass
```

### Examples

**Example 1:**
```
Input:  episode_lengths = [15, 45, 32, 67, 22, 59, 70]
Output: (2, 3, 2)
```

**Example 2:**
```
Input:  episode_lengths = [10, 25, 30, 45, 55, 65, 80]
Output: (2, 3, 2)
```

**Example 3:**
```
Input:  episode_lengths = [30, 30, 30, 30, 30]
Output: (0, 5, 0)
Explanation: 30 counts in the 30-to-60 range.
```

---

## Problem 2: Identify Longest Episode

### Description

Given a list `durations` of episode durations, write a function `prob02()` that returns the duration of the longest episode. If several episodes share the maximum duration, return that duration.

### Function Signature

```python
def prob02(durations):
    pass
```

### Examples

**Example 1:**
```
Input:  durations = [30, 45, 60, 45, 30]
Output: 60
```

**Example 2:**
```
Input:  durations = [20, 30, 40, 40, 30, 20]
Output: 40
```

**Example 3:**
```
Input:  durations = [55, 60, 55, 60, 60]
Output: 60
```

---

## Problem 3: Find Most Frequent Episode Length

### Description

Given a list `episode_lengths`, write a function `prob03()` that returns the episode length that occurs most often. If several lengths tie for the highest frequency, return the smallest one.

### Function Signature

```python
def prob03(episode_lengths):
    pass
```

### Examples

**Example 1:**
```
Input:  episode_lengths = [30, 45, 30, 60, 45, 30]
Output: 30
```

**Example 2:**
```
Input:  episode_lengths = [20, 20, 30, 30, 40, 40, 40]
Output: 40
```

**Example 3:**
```
Input:  episode_lengths = [50, 60, 70, 80, 90, 100]
Output: 50
```

---

## Problem 4: Find Median Episode Length

### Description

Given a list `durations` of episode durations, write a function `prob04()` that returns the median episode length. The median is the middle value of the sorted list. If the list has an even number of elements, return the average of the two middle values.

### Function Signature

```python
def prob04(durations):
    pass
```

### Examples

**Example 1:**
```
Input:  durations = [45, 30, 60, 30, 90]
Output: 45
```

**Example 2:**
```
Input:  durations = [90, 80, 60, 70, 50]
Output: 70
```

**Example 3:**
```
Input:  durations = [30, 10, 20, 40, 30, 50]
Output: 30.0
```

---

## Problem 5: Find Unique Genres with Minimum Episode Length

### Description

You are given a list `episodes` of `(title, genre, length)` tuples and an integer `threshold`. Write a function `prob05()` that returns the unique genres that have **at least one** episode with length greater than or equal to `threshold`, sorted alphabetically.

_Note: the source text says a genre's **shortest** episode must meet the threshold, but every example follows the "at least one episode" rule above (e.g. Art with lengths 25 and 30 passes threshold 30). This description and the tests follow the examples._

### Function Signature

```python
def prob05(episodes, threshold):
    pass
```

### Examples

**Example 1:**
```
Input:  episodes = [("Episode 1", "Tech", 30), ("Episode 2", "Health", 45), ("Episode 3", "Tech", 35),
                    ("Episode 4", "Entertainment", 60)],
        threshold = 30
Output: ['Entertainment', 'Health', 'Tech']
```

**Example 2:**
```
Input:  episodes = [("Episode A", "Science", 40), ("Episode B", "Science", 50), ("Episode C", "Art", 25),
                    ("Episode D", "Art", 30)],
        threshold = 30
Output: ['Art', 'Science']
```

**Example 3:**
```
Input:  episodes = [("Episode X", "Music", 20), ("Episode Y", "Music", 15), ("Episode Z", "Drama", 25)],
        threshold = 20
Output: ['Drama', 'Music']
```

---

## Problem 6: Find Recent Podcast Episodes

### Description

You are building a podcast management system that tracks the most recent episodes. Given a list `episodes` of unique episode IDs in the order they were added, and an integer `n`, write a function `prob06()` that returns the `n` most recent episodes, newest first. If `n` is larger than the number of episodes, return all of them, newest first.

_Note: the source text says "in the order they were added", but every example returns the episodes newest first. This description and the tests follow the examples._

### Function Signature

```python
def prob06(episodes, n):
    pass
```

### Examples

**Example 1:**
```
Input:  episodes = ['episode1', 'episode2', 'episode3', 'episode4'], n = 3
Output: ['episode4', 'episode3', 'episode2']
```

**Example 2:**
```
Input:  episodes = ['ep1', 'ep2', 'ep3'], n = 2
Output: ['ep3', 'ep2']
```

**Example 3:**
```
Input:  episodes = ['a', 'b', 'c', 'd'], n = 5
Output: ['d', 'c', 'b', 'a']
```

---

## Problem 7: Reorder Podcast Episodes

### Description

A podcast app lets users reorder their episodes, which start in a stack (LIFO order). Write a function `prob07()` that takes the list `stack` and a list `indices`, and returns the reordered list of episodes.

The indices are 0-based: `indices[i]` is the new position of the episode originally at index `i`. For example, with episodes `[A, B, C, D]` and indices `[2, 0, 3, 1]`, the episode at index 0 moves to index 2, the episode at index 1 moves to index 0, and so on.

### Function Signature

```python
def prob07(stack, indices):
    pass
```

### Examples

**Example 1:**
```
Input:  stack = ['Episode1', 'Episode2', 'Episode3', 'Episode4'], indices = [2, 0, 3, 1]
Output: ['Episode2', 'Episode4', 'Episode1', 'Episode3']
```

**Example 2:**
```
Input:  stack = ['A', 'B', 'C', 'D'], indices = [1, 2, 3, 0]
Output: ['D', 'A', 'B', 'C']
```

**Example 3:**
```
Input:  stack = ['Alpha', 'Beta', 'Gamma'], indices = [0, 2, 1]
Output: ['Alpha', 'Gamma', 'Beta']
```

### Constraints

- `indices` is a permutation of `0` to `len(stack) - 1`

---

## Problem 8: Find Longest Consecutive Listen Gaps

### Description

A podcast app helps users see the longest stretch between listening to consecutive episodes. Given a list `timestamps` of listen times (in minutes since midnight), sorted in ascending order, write a function `prob08()` that returns the longest gap between consecutive listens.

### Function Signature

```python
def prob08(timestamps):
    pass
```

### Examples

**Example 1:**
```
Input:  timestamps = [30, 50, 70, 100, 120, 150]
Output: 30
```

**Example 2:**
```
Input:  timestamps = [10, 20, 30, 50, 60, 90]
Output: 30
```

**Example 3:**
```
Input:  timestamps = [5, 10, 15, 25, 35, 45]
Output: 10
```

### Constraints

- `timestamps` is sorted in ascending order

---
