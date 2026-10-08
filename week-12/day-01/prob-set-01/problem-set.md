# Problem Set: Dynamic Programming (Avatar) — Week 12, Day 1

For Problems 1, 2, 3, and 5, also evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

---

## Problem 1: Aang's Meditation for Energy Balance

### Description

Aang balances his spiritual energy through meditation. Each day, the energy he gains is the sum of the energy he gained on the two previous days. On days 1 and 2, he gains 1 unit each.

Write a function `prob01()` that takes an integer `n` and returns the energy Aang gains on day `n`. Use a dynamic programming approach.

### Function Signature

```python
def prob01(n: int) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  n = 1
Output: 1
```

**Example 2:**
```
Input:  n = 2
Output: 1
```

**Example 3:**
```
Input:  n = 5
Output: 5
```

**Example 4:**
```
Input:  n = 7
Output: 13
```

---

## Problem 2: Toph's Earthbending Training

### Description

Toph climbs a staircase of rock steps. The integer list `cost` gives the energy to step on each step: `cost[i]` is the cost of step `i`. After paying for a step, she can climb one or two steps. She can start on step `0` or step `1`.

Write a function `prob02()` that returns the minimum energy needed to reach the top (past the last step).

### Function Signature

```python
def prob02(cost: list[int]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  cost = [10, 15, 20]
Output: 15
Explanation: Start at index 1, pay 15, and jump two steps to the top.
```

**Example 2:**
```
Input:  cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
```

---

## Problem 3: Aang and Zuko's Elemental Duel

### Description

Aang and Zuko take turns in a duel, with Aang going first. The duel starts with a number `n`, the strength of the elements on the battlefield. On each turn, a player must:

1. Choose any `x` such that `0 < x < n` and `n % x == 0`.
2. Replace `n` with `n - x`.

A player who cannot make a move loses. Write a function `prob03()` that returns `True` if Aang wins when both play optimally, and `False` otherwise.

### Function Signature

```python
def prob03(n: int) -> bool:
    pass
```

### Examples

**Example 1:**
```
Input:  n = 2
Output: True
Explanation: Aang reduces the strength by 1, and Zuko has no moves.
```

**Example 2:**
```
Input:  n = 3
Output: False
Explanation: Aang reduces by 1, then Zuko reduces by 1, leaving Aang with no moves.
```

---

## Problem 4: Aang's Training Sequence

### Description

The string `sequence` is a flow of bending techniques, and the string `move` is one technique. `move` is **k-repeating** if `move` repeated `k` times is a substring of `sequence`. Its **maximum k-repeating value** is the largest such `k`, or `0` if `move` is not a substring of `sequence`.

Write a function `prob04()` that uses dynamic programming to return the maximum k-repeating value of `move` in `sequence`.

### Function Signature

```python
def prob04(sequence: str, move: str) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  sequence = "airairwater", move = "air"
Output: 2
Explanation: "airair" is a substring of "airairwater".
```

**Example 2:**
```
Input:  sequence = "fireearthfire", move = "fire"
Output: 1
Explanation: "fire" is a substring, but "firefire" is not.
```

**Example 3:**
```
Input:  sequence = "waterfire", move = "air"
Output: 0
```

---

## Problem 5: Zuko's Redemption Mission

### Description

Zuko is gathering supplies for the Earth Kingdom. The integer list `tokens` gives the supply value of each token type, and he has an unlimited number of each. Write a function `prob05()` that returns the fewest tokens needed to gather exactly `amount` units, or `-1` if it is impossible.

### Function Signature

```python
def prob05(tokens: list[int], amount: int) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  tokens = [1, 2, 5], amount = 11
Output: 3
Explanation: 5 + 5 + 1 = 11.
```

**Example 2:**
```
Input:  tokens = [2], amount = 3
Output: -1
```

**Example 3:**
```
Input:  tokens = [1], amount = 0
Output: 0
```

---

## Problem 6: Toph and Katara's Training Synchronization

### Description

Toph and Katara want to synchronize their training. A synchronized sequence is a common subsequence of both routines. A **subsequence** is formed by deleting some characters from a string without changing the order of the rest.

Given strings `katara_moves` and `toph_moves`, write a function `prob06()` that uses dynamic programming to return the length of their longest common subsequence, or `0` if there is none.

_2-D dynamic programming is an extra challenge for TIP102 (in scope for TIP103)._

### Function Signature

```python
def prob06(katara_moves: str, toph_moves: str) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  katara_moves = "waterbend", toph_moves = "earthbend"
Output: 6
Explanation: "erbend" is a longest common subsequence.
```

**Example 2:**
```
Input:  katara_moves = "bend", toph_moves = "bend"
Output: 4
```

**Example 3:**
```
Input:  katara_moves = "fire", toph_moves = "air"
Output: 2
Explanation: "ir"
```

---
