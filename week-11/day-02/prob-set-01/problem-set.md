# Problem Set: Graphs in Grids II (Zombies) — Week 11, Day 2

For every problem, also evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

---

## Problem 1: Nearest Zombie

### Description

Given an `m x n` binary matrix `grid`, where `1` is a human and `0` is a zombie, write a function `prob01()` that returns a matrix of the same size where each cell holds the distance from that square to the nearest zombie.

The distance between two horizontally or vertically adjacent cells is 1.

### Function Signature

```python
def prob01(grid: list[list[int]]) -> list[list[int]]:
    pass
```

### Examples

**Example 1:**
```
Input:  grid = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
Output: [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]
```

**Example 2:**
```
Input:  grid = [[0, 0, 0],
                [0, 1, 0],
                [1, 1, 1]]
Output: [[0, 0, 0],
         [0, 1, 0],
         [1, 2, 1]]
```

---

## Problem 2: Defending the Safehouse

### Description

The city is a binary `m x n` matrix `city`, where `1` is an accessible passage and `0` is a blocked area. You can only move **down** (`row + 1, col`) or **right** (`row, col + 1`) through accessible passages. You start at the top-left corner `(0, 0)`, and the safehouse is at the bottom-right corner `(m - 1, n - 1)`.

Flipping a cell changes it from `0` to `1` or from `1` to `0`. Write a function `prob02()` that returns `True` if you can disconnect the safehouse (leave no path from `(0, 0)` to `(m - 1, n - 1)`) by flipping **at most one** cell, never flipping `(0, 0)` or `(m - 1, n - 1)`. Otherwise return `False`.

### Function Signature

```python
def prob02(city: list[list[int]]) -> bool:
    pass
```

### Examples

**Example 1:**
```
Input:  city = [[1, 1, 1],
                [0, 0, 1],
                [1, 1, 1]]
Output: True
Explanation: Flipping any of (0, 1), (0, 2), or (1, 2) disconnects the safehouse.
```

**Example 2:**
```
Input:  city = [[1, 0, 0],
                [1, 1, 0],
                [0, 1, 1]]
Output: True
Explanation: Flipping (1, 1) disconnects the safehouse.
```

---

## Problem 3: Zombie Infested City Regions

### Description

The city is an `n x n` grid given as a list of strings: each string is a row, and each character is one `1 x 1` square. A square holds:

- `'/'` or `'\\'`: a fence dividing the square into two triangles.
- `' '`: an open area with no division.

Write a function `prob03()` that returns the total number of contiguous regions.

Backslashes are written `'\\'` in Python because `\` is an escape character.

_Note: the source's third example, `["/\","\/"]`, is not valid Python; it should be `["/\\", "\\/"]`._

### Function Signature

```python
def prob03(grid: list[str]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  grid = [" /", "/ "]
Output: 2
```

**Example 2:**
```
Input:  grid = [" /", "  "]
Output: 1
```

**Example 3:**
```
Input:  grid = ["/\\", "\\/"]
Output: 5
Explanation: "/\\" is the row /\ and "\\/" is the row \/.
```

---

## Problem 4: Escape the Infected Zone

### Description

You are trapped in a rectangular infected zone. The Pacific Safety Zone borders its **left and top** edges, and the Atlantic Safety Zone borders its **right and bottom** edges.

The zone is a grid of subzones given by an `m x n` integer matrix `safety`, where `safety[row][column]` is the safety level of that subzone. Survivors can move north, south, east, or west to a neighbor only if the neighbor's safety level is **less than or equal to** the current one. A subzone on an edge can step straight out to the safety zone bordering that edge.

Write a function `prob04()` that returns a list of `[row, column]` coordinates of every subzone from which survivors can reach **both** safety zones. The coordinates may be in any order.

_Note: the source gives `[[0, 0], [1, 1]]` for Example 2, but all four subzones of that grid can reach both zones. For example, `[0, 1]` sits on the top edge (Pacific) and the right edge (Atlantic)._

### Function Signature

```python
def prob04(safety: list[list[int]]) -> list[list[int]]:
    pass
```

### Examples

**Example 1:**
```
Input:  safety = [[1, 2, 2, 3, 5],
                  [3, 2, 3, 4, 4],
                  [2, 4, 5, 3, 1],
                  [6, 7, 1, 4, 5],
                  [5, 1, 1, 2, 4]]
Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
Explanation: For example, from [2, 2]: [2, 2] -> [1, 2] -> [0, 2] -> Pacific,
and [2, 2] -> [2, 3] -> [2, 4] -> Atlantic.
```

**Example 2:**
```
Input:  safety = [[2, 1],
                  [1, 2]]
Output: [[0, 0], [0, 1], [1, 0], [1, 1]]
```

---

## Problem 5: Decreasing Zombie Path

### Description

Given an `m x n` matrix `city`, where each cell holds the number of zombies in that area, write a function `prob05()` that returns the length of the longest **strictly decreasing** path through the city. You move between horizontally or vertically adjacent cells, each next cell must have strictly fewer zombies than the one before, and no cell may be visited twice.

_Note: the source defines the second grid as `city_` but prints `city_2`._

### Function Signature

```python
def prob05(city: list[list[int]]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  city = [[4, 3],
                [1, 2]]
Output: 4
Explanation: 4 -> 3 -> 2 -> 1
```

**Example 2:**
```
Input:  city = [[1, 2, 18, 3],
                [26, 6, 7, 15],
                [9, 10, 17, 18],
                [14, 15, 16, 22]]
Output: 9
Explanation: 22 -> 18 -> 17 -> 16 -> 15 -> 10 -> 6 -> 2 -> 1
```

---
