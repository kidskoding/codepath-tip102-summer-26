# Problem Set: Strings & Arrays (Batman) — Week 1, Day 2

---

## Problem 1: String Array Equivalency

### Description

Given two string lists `word1` and `word2`, write a function `prob01()` that returns `True` if the two lists represent the same string, and `False` otherwise.

A list represents a string if its elements, concatenated in order, form that string.

### Function Signature

```python
def prob01(word1, word2):
    pass
```

### Examples

**Example 1:**
```
Input:  word1 = ["bat", "man"], word2 = ["b", "atman"]
Output: True
```

**Example 2:**
```
Input:  word1 = ["alfred", "pennyworth"], word2 = ["alfredpenny", "word"]
Output: False
```

**Example 3:**
```
Input:  word1 = ["cat", "wom", "an"], word2 = ["catwoman"]
Output: True
```

---

## Problem 2: Count Even Strings

### Description

Write a function `prob02()` that accepts a list of strings `lst` and returns the number of strings in the list with an even length.

### Function Signature

```python
def prob02(lst):
    pass
```

### Examples

**Example 1:**
```
Input:  lst = ["na", "nana", "nanana", "batman", "!"]
Output: 4
```

**Example 2:**
```
Input:  lst = ["the", "joker", "robin"]
Output: 0
```

**Example 3:**
```
Input:  lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
Output: 9
```

---

## Problem 3: Secret Identity

### Description

Write a function `prob03()` to keep Batman's secret identity hidden. The function accepts a list of names `people` and a string `secret_identity`, and returns the list with every instance of `secret_identity` removed.

**A solution is considered valid if:**
- The list is modified in place — no new lists are created
- The relative order of the remaining elements is maintained

### Function Signature

```python
def prob03(people, secret_identity):
    pass
```

### Examples

**Example 1:**
```
Input:  people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne'], secret_identity = 'Bruce Wayne'
Output: ['Batman', 'Superman', 'The Riddler']
```

---

## Problem 4: Count Digits

### Description

Given a non-negative integer `n`, write a function `prob04()` that returns the number of digits in `n`. You may not cast `n` to a string.

### Function Signature

```python
def prob04(n):
    pass
```

### Examples

**Example 1:**
```
Input:  n = 964
Output: 3
```

**Example 2:**
```
Input:  n = 0
Output: 1
```

### Constraints

- `n >= 0`
- Do not convert `n` to a string

---

## Problem 5: Move Zeroes

### Description

Write a function `prob05()` that accepts an integer list `lst` and returns a new list with all `0`s moved to the end. The relative order of the non-zero elements must be maintained.

### Function Signature

```python
def prob05(lst):
    pass
```

### Examples

**Example 1:**
```
Input:  lst = [1, 0, 2, 0, 3, 0]
Output: [1, 2, 3, 0, 0, 0]
```

---

## Problem 6: Reverse Vowels of a String

### Description

Given a string `s`, write a function `prob06()` that reverses only the vowels in the string and returns the result.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`. They can appear in both lowercase and uppercase, and more than once.

### Function Signature

```python
def prob06(s):
    pass
```

### Examples

**Example 1:**
```
Input:  s = "robin"
Output: "ribon"
```

**Example 2:**
```
Input:  s = "BATgirl"
Output: "BiTgArl"
```

**Example 3:**
```
Input:  s = "batman"
Output: "batman"
```

---

## Problem 7: Vantage Point

### Description

Batman is scouting an area where he thinks Harley Quinn might commit her next crime spree. The area has many hills of different heights, and Batman wants the tallest one for the best vantage point. His trip consists of `n + 1` points at different altitudes. He starts at point `0` with altitude `0`.

Write a function `prob07()` that accepts an integer list `gain` of length `n`, where `gain[i]` is the net gain in altitude between points `i` and `i + 1` for all `0 <= i < n`. Return the highest altitude of any point.

### Function Signature

```python
def prob07(gain):
    pass
```

### Examples

**Example 1:**
```
Input:  gain = [-5, 1, 5, 0, -7]
Output: 1
```

**Example 2:**
```
Input:  gain = [-4, -3, -2, -1, 4, 3, 2]
Output: 0
```

---

## Problem 8: Left and Right Sum Differences

### Description

Given a 0-indexed integer list `nums`, write a function `prob08()` that returns a 0-indexed integer list `answer` where:

- `len(answer) == len(nums)`
- `answer[i] = left_sum[i] - right_sum[i]`

Where:

- `left_sum[i]` is the sum of elements to the left of index `i` in `nums`. If there are none, `left_sum[i] = 0`.
- `right_sum[i]` is the sum of elements to the right of index `i` in `nums`. If there are none, `right_sum[i] = 0`.

### Function Signature

```python
def prob08(nums):
    pass
```

### Examples

**Example 1:**
```
Input:  nums = [10, 4, 8, 3]
Output: [-15, -1, 11, 22]
```

**Example 2:**
```
Input:  nums = [1]
Output: [0]
```

---

## Problem 9: Common Cause

### Description

Write a function `prob09()` that takes in two lists `lst1` and `lst2` and returns a list of the elements common to both lists.

### Function Signature

```python
def prob09(lst1, lst2):
    pass
```

### Examples

**Example 1:**
```
Input:  lst1 = ["super strength", "super speed", "x-ray vision"], lst2 = ["super speed", "time travel", "dimensional travel"]
Output: ["super speed"]
```

**Example 2:**
```
Input:  lst1 = ["super strength", "super speed", "x-ray vision"], lst2 = ["martial arts", "stealth", "master detective"]
Output: []
```

---

## Problem 10: Exposing Superman

### Description

Metropolis has a population of `n`, with each citizen assigned an integer id from `1` to `n`. Rumor says Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:

1. Superman trusts nobody.
2. Everybody (except Superman) trusts Superman.
3. Exactly one citizen satisfies properties 1 and 2.

Write a function `prob10()` that accepts a 2D list `trust`, where `trust[i] = [a_i, b_i]` means the person labeled `a_i` trusts the person labeled `b_i`, and the population size `n`. If a trust relationship is not in `trust`, it does not exist.

Return the label of Superman if he is hiding among the population and can be identified, or `-1` otherwise.

### Function Signature

```python
def prob10(trust, n):
    pass
```

### Examples

**Example 1:**
```
Input:  n = 2, trust = [[1, 2]]
Output: 2
```

**Example 2:**
```
Input:  n = 3, trust = [[1, 3], [2, 3]]
Output: 3
```

**Example 3:**
```
Input:  n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
```

---
