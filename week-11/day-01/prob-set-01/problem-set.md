# Problem Set: Grid Graphs (Zombie Apocalypse) — Week 11, Day 1

For every problem, also evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

In every grid, you may move to the cell directly up, down, left, or right of your current cell, as long as it is inside the grid.

---

## Problem 1: Seeking Safety

### Description

The city is overrun by zombies. You have a map of the city as an `m x n` matrix `grid` of `1`s (safe zones) and `0`s (infected zones). Given your current `position` as a `(row, column)` tuple, write a function `prob01()` that returns a list of the safe next moves, in any order.

A move goes to a horizontally or vertically adjacent cell whose row and column are both valid indices in `grid`. A move is safe if that cell has value `1`.

### Function Signature

```python
def prob01(position: tuple[int, int], grid: list[list[int]]) -> list[tuple[int, int]]:
    pass
```

### Examples

```
grid = [
    [0, 0, 0, 1, 1],  # Row 0
    [0, 0, 0, 1, 1],  # Row 1
    [1, 1, 1, 0, 0],  # Row 2
    [1, 1, 1, 1, 0],  # Row 3
    [0, 0, 0, 1, 0]   # Row 4
]
```

**Example 1:**
```
Input:  position = (3, 2), grid
Output: [(3, 1), (3, 3), (2, 2)]
Explanation: The cells left, right, and up from (3, 2) are 1s. The cell below is 0, so it is unsafe.
```

**Example 2:**
```
Input:  position = (0, 4), grid
Output: [(0, 3), (1, 4)]
Explanation: Left and down are safe. Up and right are out of bounds.
```

**Example 3:**
```
Input:  position = (0, 1), grid
Output: []
Explanation: Every neighbor of (0, 1) is either 0 or out of bounds.
```

---

## Problem 2: Escape to the Safe Haven

### Description

A safe haven is at the bottom-right corner of the city, an `m x n` matrix `grid` where `1`s are safe zones and `0`s are infected zones. Given your current `position` as a `(row, column)` tuple, write a function `prob02()` that returns `True` if you can reach the safe haven moving only through safe zones, and `False` otherwise.

Your starting cell itself may be infected (`0`); you only need every cell you move *into* to be safe.

### Function Signature

```python
def prob02(position: tuple[int, int], grid: list[list[int]]) -> bool:
    pass
```

### Examples

```
grid = [
    [1, 0, 1, 1, 0],  # Row 0
    [1, 1, 1, 1, 0],  # Row 1
    [0, 0, 1, 1, 0],  # Row 2
    [1, 0, 1, 1, 1]   # Row 3
]
```

**Example 1:**
```
Input:  position = (0, 0), grid
Output: True
Explanation: (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> (2, 2) -> (3, 2) -> (3, 3) -> (3, 4)
```

**Example 2:**
```
Input:  position = (0, 4), grid
Output: True
Explanation: You start in an infected zone, but can step straight into the safe zone (0, 3)
and travel safely from there to (3, 4).
```

**Example 3:**
```
Input:  position = (3, 0), grid
Output: False
```

---

## Problem 3: List All Escape Routes

### Description

Given an `m x n` grid `grid` of the city, write a function `prob03()` that returns a list of `(row, column)` tuples for every starting cell from which there is a path of safe zones (`1`s) to the safe haven in the bottom-right corner. A starting cell with value `0` is infected and cannot reach the safe haven. Return the cells in any order.

### Function Signature

```python
def prob03(grid: list[list[int]]) -> list[tuple[int, int]]:
    pass
```

### Examples

**Example 1:**
```
Input:  grid = [
            [1, 0, 1, 0, 1],  # Row 0
            [1, 1, 1, 1, 0],  # Row 1
            [0, 0, 1, 0, 0],  # Row 2
            [1, 0, 1, 1, 1]   # Row 3
        ]
Output: [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]
```

---

## Problem 4: Largest Safe Zone

### Description

Given an `m x n` grid `grid` where `1`s are safe zones and `0`s are infected zones, write a function `prob04()` that returns the area of the largest group of connected safe zones. Each cell has an area of 1, and cells are connected to the cells up, down, left, and right of them.

### Function Signature

```python
def prob04(grid: list[list[int]]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  grid = [
            [0, 0, 0, 1, 1],  # Row 0
            [0, 0, 0, 1, 1],  # Row 1
            [1, 1, 1, 0, 0],  # Row 2
            [1, 1, 1, 1, 0],  # Row 3
            [0, 0, 0, 1, 0]   # Row 4
        ]
Output: 8
Explanation: The group starting in row 0 has size 4. The group starting in row 2 has size 8.
```

---

## Problem 5: Zombie Spread

### Description

The city is a 2D grid `grid` where:

- `0` is an obstacle where neither humans nor zombies can live,
- `1` is a human safe zone,
- `2` is a zone already infected by zombies.

Every hour, each infected zone infects its adjacent safe zones (up, down, left, right). Write a function `prob05()` that returns the number of hours until every safe zone is infected. If some safe zones can never be infected, return `-1`.

### Function Signature

```python
def prob05(grid: list[list[int]]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  grid = [[2, 1, 1],
                [1, 1, 0],
                [0, 1, 1]]
Output: 4
```

**Example 2:**
```
Input:  grid = [[2, 1, 1],
                [0, 1, 1],
                [1, 0, 1]]
Output: -1
Explanation: The safe zone at (2, 0) is never infected, since infection only spreads up, down, left, and right.
```

**Example 3:**
```
Input:  grid = [[0, 2]]
Output: 0
Explanation: There are no safe zones to begin with.
```

---
