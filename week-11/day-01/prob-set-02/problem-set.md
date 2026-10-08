# Problem Set: Grid Graphs (Kingdom Battles) — Week 11, Day 1

For every problem, also evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

In every grid, you may move to the cell directly up, down, left, or right of your current cell, as long as it is inside the grid.

---

## Problem 1: Battle Moves

### Description

You have an `m x n` matrix `battle` of the battlefield, where each cell is `'X'` (your kingdom's territory) or `'O'` (the opposing kingdom's territory). Given your current `row` and `column`, and a list `past_moves` of `(row, column)` tuples you have already taken, write a function `prob01()` that returns a list of valid next moves, in any order.

A valid move goes to a horizontally or vertically adjacent cell that is inside the grid, is `'X'`, and is not in `past_moves`.

### Function Signature

```python
def prob01(battle: list[list[str]], row: int, column: int, past_moves: list[tuple[int, int]]) -> list[tuple[int, int]]:
    pass
```

### Examples

```
battle = [
    ['X', 'O', 'O', 'X', 'X'],  # Row 0
    ['O', 'O', 'O', 'X', 'X'],  # Row 1
    ['X', 'X', 'X', 'O', 'O'],  # Row 2
    ['X', 'X', 'X', 'X', 'O'],  # Row 3
    ['O', 'O', 'O', 'X', 'O']   # Row 4
]
```

**Example 1:**
```
Input:  battle, row = 3, column = 2, past_moves = []
Output: [(3, 1), (3, 3), (2, 2)]
```

**Example 2:**
```
Input:  battle, row = 3, column = 2, past_moves = [(2, 2), (3, 3), (0, 0)]
Output: [(3, 1)]
Explanation: (3, 3) and (2, 2) were already taken.
```

**Example 3:**
```
Input:  battle, row = 0, column = 4, past_moves = []
Output: [(0, 3), (1, 4)]
Explanation: Up and right are out of bounds.
```

**Example 4:**
```
Input:  battle, row = 0, column = 0, past_moves = []
Output: []
Explanation: Every neighbor is enemy territory or out of bounds.
```

---

## Problem 2: Castle Path

### Description

Your kingdom is an `m x n` matrix `kingdom` of towns. Towns safe to travel through are `'X'`, and towns with dangerous bandits are `'O'`. Given your current `town` and the `castle` location as `(row, column)` tuples, write a function `prob02()` that returns a list of `(row, column)` tuples giving a shortest path from `town` to `castle` that never enters a bandit town. If there are several shortest paths, return any one. If no such path exists (including when `town` itself is a bandit town), return `None`.

### Function Signature

```python
def prob02(kingdom: list[list[str]], town: tuple[int, int], castle: tuple[int, int]) -> list[tuple[int, int]] | None:
    pass
```

### Examples

```
kingdom = [
    ['X', 'O', 'X', 'X', 'O'],  # Row 0
    ['X', 'X', 'X', 'X', 'O'],  # Row 1
    ['O', 'O', 'X', 'X', 'O'],  # Row 2
    ['X', 'O', 'X', 'X', 'X']   # Row 3
]
castle = (3, 4)
```

**Example 1:**
```
Input:  kingdom, town = (0, 0), castle
Output: [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4)]
Explanation: Other shortest paths of the same length are also accepted.
```

**Example 2:**
```
Input:  kingdom, town = (0, 4), castle
Output: None
Explanation: (0, 4) is a bandit town.
```

**Example 3:**
```
Input:  kingdom, town = (3, 0), castle
Output: None
```

---

## Problem 3: Walls and Gates

### Description

You have an `m x n` grid `castle` where each cell is one of:

- `-1`: a wall or obstacle
- `0`: a gate
- `float('inf')`: an empty room

Write a function `prob03()` that modifies `castle` **in place** so each empty room holds its distance to the nearest gate, and returns `castle`. A room that cannot reach any gate stays `float('inf')`.

### Function Signature

```python
def prob03(castle: list[list[float]]) -> list[list[float]]:
    pass
```

### Examples

**Example 1:**
```
Input:  castle = [
            [inf, -1,  0,   inf],  # Row 0
            [inf, inf, inf, -1],   # Row 1
            [inf, -1,  inf, -1],   # Row 2
            [0,   -1,  inf, inf]   # Row 3
        ]
Output: [
            [3, -1, 0,  1],
            [2,  2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3,  4]
        ]
```

(`inf` is `float('inf')`.)

---

## Problem 4: Surrounded Regions

### Description

You are given an `m x n` matrix `map` of `'X'` (your territory) and `'O'` (the opposing kingdom's territory). Cells connect horizontally and vertically, and a **region** is a group of connected cells with the same letter. An `'O'` region is **surrounded**, and can be captured, if none of its cells lie on the edge of the map.

Write a function `prob04()` that captures every surrounded region by replacing its `'O'`s with `'X'`s **in place**, and returns `map`.

### Function Signature

```python
def prob04(map: list[list[str]]) -> list[list[str]]:
    pass
```

### Examples

**Example 1:**
```
Input:  map = [["X", "X", "X", "X"],
               ["X", "O", "O", "X"],
               ["X", "X", "O", "X"],
               ["X", "O", "X", "X"]]
Output: [["X", "X", "X", "X"],
         ["X", "X", "X", "X"],
         ["X", "X", "X", "X"],
         ["X", "O", "X", "X"]]
Explanation: The bottom 'O' is on the edge of the map, so it cannot be surrounded.
```

---

## Problem 5: Maximum Number of Troops Captured

### Description

You are given an `m x n` matrix `battlefield`, where `battlefield[row][column]` is:

- `0`: an impassable obstacle, or
- a positive number: that many enemy troops on the square.

Your kingdom may start on any non-obstacle square and, any number of times, capture all troops on its current square or move to an adjacent (up, down, left, right) square that has troops. Write a function `prob05()` that returns the maximum number of troops you can capture with the best starting square, or `0` if there are no troops.

### Function Signature

```python
def prob05(battlefield: list[list[int]]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  battlefield = [[0, 2, 1, 0],
                       [4, 0, 0, 3],
                       [1, 0, 0, 4],
                       [0, 3, 2, 0]]
Output: 7
Explanation: Start at (1, 3) and capture 3 troops, then move to (2, 3) and capture 4.
```

**Example 2:**
```
Input:  battlefield = [[1, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 1]]
Output: 1
Explanation: Start at (0, 0) or (3, 3) and capture a single troop.
```

---
