# Problem Set: Stacks, Queues & Two Pointers (Streaming) — Week 3, Day 1

---

## Problem 1: Time Needed to Stream Movies

### Description

There are `n` users in a queue waiting to stream movies. User `0` is at the front of the queue and user `n - 1` is at the back.

You are given a 0-indexed integer list `movies` of length `n`, where `movies[i]` is the number of movies user `i` wants to stream.

Each user takes exactly 1 second to stream one movie. A user streams only 1 movie at a time, then goes to the back of the queue (instantly) to stream more. A user with no movies left leaves the queue.

Write a function `prob01()` that returns the time taken for the user at position `k` (0-indexed) to finish streaming all their movies.

### Function Signature

```python
def prob01(movies, k):
    pass
```

### Examples

**Example 1:**
```
Input:  movies = [2, 3, 2], k = 2
Output: 6
```

**Example 2:**
```
Input:  movies = [5, 1, 1, 1], k = 0
Output: 8
```

---

## Problem 2: Reverse Watchlist

### Description

You are given a list `watchlist` of shows sorted by popularity. The user wants to discover new shows by seeing the least popular shows first.

Using the two-pointer approach, write a function `prob02()` that reverses `watchlist` in place: the first show becomes the last, the second becomes the second to last, and so on. Return the reversed list.

**A solution is considered valid if:**
- The list is reversed in place
- It does not use list slicing (e.g. `watchlist[::-1]`)

### Function Signature

```python
def prob02(watchlist):
    pass
```

### Examples

**Example 1:**
```
Input:  watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]
Output: ['The Witcher', 'The Crown', 'Stranger Things', 'Breaking Bad']
```

---

## Problem 3: Remove All Adjacent Duplicate Shows

### Description

You are given a string `schedule` representing the lineup of shows on a streaming platform, where each character is a different show. A duplicate removal chooses two adjacent, equal shows and removes them from the schedule.

Repeat duplicate removals on `schedule` until no more can be made. Write a function `prob03()` that returns the final schedule. The answer is guaranteed to be unique.

### Function Signature

```python
def prob03(schedule):
    pass
```

### Examples

**Example 1:**
```
Input:  schedule = "abbaca"
Output: "ca"
```

**Example 2:**
```
Input:  schedule = "azxxzy"
Output: "ay"
```

---

## Problem 4: Minimum Average of Smallest and Largest View Counts

### Description

You are given a list `view_counts` of `n` integers, where `n` is even. Repeat this procedure `n / 2` times:

1. Remove the smallest view count, `min_view_count`, and the largest view count, `max_view_count`, from `view_counts`.
2. Add `(min_view_count + max_view_count) / 2` to the list `average_views`.

Write a function `prob04()` that returns the minimum element in `average_views`.

### Function Signature

```python
def prob04(view_counts):
    pass
```

### Examples

**Example 1:**
```
Input:  view_counts = [7, 8, 3, 4, 15, 13, 4, 1]
Output: 5.5
```

**Example 2:**
```
Input:  view_counts = [1, 9, 8, 3, 10, 5]
Output: 5.5
```

**Example 3:**
```
Input:  view_counts = [1, 2, 3, 7, 8, 9]
Output: 5.0
```

### Constraints

- `len(view_counts)` is even

---

## Problem 5: Minimum Remaining Watchlist After Removing Movies

### Description

You have a string `watchlist` of uppercase English letters, where each letter represents a movie. In one operation, you can remove any occurrence of the pair `"AB"` or `"CD"` from `watchlist`.

After a removal, the remaining parts join together, which can create new `"AB"` or `"CD"` pairs.

Write a function `prob05()` that returns the minimum possible length of the watchlist after any number of operations.

### Function Signature

```python
def prob05(watchlist):
    pass
```

### Examples

**Example 1:**
```
Input:  watchlist = "ABFCACDB"
Output: 2
```

**Example 2:**
```
Input:  watchlist = "ACBBD"
Output: 5
```

---

## Problem 6: Apply Operations to Show Ratings

### Description

You are given a 0-indexed list `ratings` of size `n` of non-negative integers, each the rating of a show.

Apply `n - 1` operations to the list. In operation `i` (0-indexed), do the following on element `i`:

- If `ratings[i] == ratings[i + 1]`, multiply `ratings[i]` by 2 and set `ratings[i + 1]` to 0. Otherwise, skip this operation.

After all operations, shift every 0 to the end of the list. For example, `[1, 0, 2, 0, 0, 1]` becomes `[1, 2, 1, 0, 0, 0]`.

Write a function `prob06()` that returns the resulting list.

### Function Signature

```python
def prob06(ratings):
    pass
```

### Examples

**Example 1:**
```
Input:  ratings = [1, 2, 2, 1, 1, 0]
Output: [1, 4, 2, 0, 0, 0]
```

**Example 2:**
```
Input:  ratings = [0, 1]
Output: [1, 0]
```

---

## Problem 7: Lexicographically Smallest Watchlist

### Description

You are given a string `watchlist` of lowercase English letters, where each letter is a show. In one operation, you can replace a letter in `watchlist` with any other lowercase letter.

Make `watchlist` a palindrome using the minimum number of operations. If several palindromes need the same minimum number of operations, make the lexicographically smallest one.

String `a` is lexicographically smaller than string `b` (of the same length) if, at the first position where they differ, `a` has the letter that comes earlier in the alphabet.

Write a function `prob07()` that returns the resulting string, by implementing this pseudocode:

1. Convert `watchlist` to a list.
2. Set a left pointer at index 0 and a right pointer at the last index.
3. While the left pointer is less than the right pointer:
   1. Compare the characters at the two pointers.
   2. If they differ, replace the alphabetically later character with the earlier one.
   3. Move the left pointer one step right and the right pointer one step left.
4. Convert the list back to a string and return it.

### Function Signature

```python
def prob07(watchlist):
    pass
```

### Examples

**Example 1:**
```
Input:  watchlist = "egcfe"
Output: "efcfe"
```

**Example 2:**
```
Input:  watchlist = "abcd"
Output: "abba"
```

**Example 3:**
```
Input:  watchlist = "seven"
Output: "neven"
```

---
