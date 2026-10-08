# Problem Set: Graphs in Grids II (Kingdom) — Week 11, Day 2

For every problem, also evaluate the time and space complexity of your solution. Define your variables and explain why your solution has the stated complexity.

---

## Problem 1: Number of Protected Towns

### Description

You are given an `m x n` binary grid `kingdom`. A **town** is a maximal group of `0`s connected vertically or horizontally. A **protected town** is a town surrounded by `1`s on all sides, which means none of its cells is on the edge of the grid.

Write a function `prob01()` that returns the number of protected towns.

### Function Signature

```python
def prob01(kingdom: list[list[int]]) -> int:
    pass
```

### Examples

**Example 1:**
```
Input:  kingdom = [[1, 1, 1, 1, 1, 1, 1, 0],
                   [1, 0, 0, 0, 0, 1, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0],
                   [1, 0, 0, 0, 0, 1, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 0]]
Output: 2
```

**Example 2:**
```
Input:  kingdom = [[0, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0],
                   [0, 1, 1, 1, 0]]
Output: 1
```

---

## Problem 2: Cyclical Roads in Kingdom

### Description

Your kingdom is an `m x n` grid `kingdom` of characters, where each character is a road. A **cyclical road** is a path of length 4 or more that starts and ends at the same square, where every square on the path holds the same character. You may move up, down, left, or right to a neighbor holding the same character, but you may not move straight back to the square you just came from. For example, `(1, 1) -> (1, 2) -> (1, 1)` is not a cycle.

Write a function `prob02()` that returns `True` if any cyclical road exists, and `False` otherwise.

### Function Signature

```python
def prob02(kingdom: list[list[str]]) -> bool:
    pass
```

### Examples

**Example 1:**
```
Input:  kingdom = [["a", "a", "a", "a"],
                   ["a", "b", "b", "a"],
                   ["a", "b", "b", "a"],
                   ["a", "a", "a", "a"]]
Output: True
```

**Example 2:**
```
Input:  kingdom = [["c", "c", "c", "a"],
                   ["c", "d", "c", "c"],
                   ["c", "c", "e", "c"],
                   ["f", "c", "c", "c"]]
Output: True
```

**Example 3:**
```
Input:  kingdom = [["a", "b", "b"],
                   ["b", "z", "b"],
                   ["b", "b", "a"]]
Output: False
```

---

## Problem 3: Escape the Dungeon

### Description

You are trapped in a dark dungeon, an `m x n` grid `dungeon` where `0` is an open passage and `1` is a wall. You can move up, down, left, or right, but once you start moving in a direction you keep going until you hit a wall. Then you can choose a new direction. The edges of the grid act as walls.

Given your starting `position` as `(start_row, start_col)` and the `exit` as `(exit_row, exit_col)`, write a function `prob03()` that returns `True` if you can **stop** at the exit, and `False` otherwise. Passing over the exit without stopping there does not count.

### Function Signature

```python
def prob03(dungeon: list[list[int]], position: tuple[int, int], exit: tuple[int, int]) -> bool:
    pass
```

### Examples

```
dungeon = [[0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 0, 0, 0]]
```

**Example 1:**
```
Input:  dungeon, position = (0, 4), exit = (4, 4)
Output: True
Explanation: One route: from (0, 4) roll left to (0, 3), down to (1, 3), left to (1, 0),
down to (2, 0), right to (2, 2), down to (4, 2), then right to (4, 4).
```

**Example 2:**
```
Input:  dungeon, position = (0, 4), exit = (3, 2)
Output: False
Explanation: You can pass through (3, 2), but you can never stop there.
```

_Note: the source's explanation for Example 1 ("roll left to (0, 1), then down to (4, 1)") is not a valid route: rolling left from (0, 4) stops at (0, 3) because (0, 2) is a wall, and column 1 is blocked at row 3. The answer, `True`, is still correct._

---

## Problem 4: Surveying the Kingdom

### Description

Your kingdom is `m x n` hectares of land, given as a binary matrix `land` where `0` is forest and `1` is farmland. Farmland comes in **farmland groups**: rectangles made entirely of farmland, where no two groups are horizontally or vertically adjacent.

The top-left corner of `land` is `(0, 0)` and the bottom-right corner is `(m - 1, n - 1)`. A group with top-left corner `(r1, c1)` and bottom-right corner `(r2, c2)` is written `[r1, c1, r2, c2]`.

Write a function `prob04()` that returns a list of every farmland group, in any order, or an empty list if there is no farmland.

_Note: the source's example grid, `[[1, 0, 0], [1, 0, 1], [1, 1, 1]]`, breaks the problem's own rules: its farmland forms one L-shaped group, not rectangles. The example below is a valid grid._

### Function Signature

```python
def prob04(land: list[list[int]]) -> list[list[int]]:
    pass
```

### Examples

**Example 1:**
```
Input:  land = [[1, 0, 0],
                [0, 1, 1],
                [0, 1, 1]]
Output: [[0, 0, 0, 0], [1, 1, 2, 2]]
Explanation: One group is the single hectare (0, 0); the other spans (1, 1) to (2, 2).
```

---

## Problem 5: Reinforce the Kingdom Walls

### Description

Your kingdom is an `m x n` integer matrix `kingdom_grid`, where each value is the defensive strength of that square. Two squares are in the same **fortified section** if they are adjacent (up, down, left, right) and have the same strength.

The **border** of a section is every square in it that is either adjacent to a square with a different strength, or on the outer edge of the kingdom.

Given `row`, `col`, and `new_strength`, write a function `prob05()` that finds the section containing `kingdom_grid[row][col]`, sets every square on its border to `new_strength`, and returns the updated `kingdom_grid`.

### Function Signature

```python
def prob05(kingdom_grid: list[list[int]], row: int, col: int, new_strength: int) -> list[list[int]]:
    pass
```

### Examples

**Example 1:**
```
Input:  kingdom_grid = [[1, 1, 1, 2],
                        [1, 3, 1, 2],
                        [1, 1, 1, 2]],
        row = 1, col = 1, new_strength = 4
Output: [[1, 1, 1, 2],
         [1, 4, 1, 2],
         [1, 1, 1, 2]]
```

---
