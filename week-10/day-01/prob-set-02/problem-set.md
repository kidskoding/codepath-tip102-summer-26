# Problem Set #2: Graphs — Week 10, Day 1

---

## Problem 1: Hollywood Stars

**Difficulty:** Easy

### Description

The graph below illustrates connections between different Hollywood stars. Each node represents a celebrity, and an edge between two nodes indicates that the celebrities know each other.

Represent this undirected graph as an adjacency dictionary where each node's value is a string with the celebrity's name (ex. `"Kevin Bacon"`).

The original problem asks for a module-level variable `hollywood_stars`. Build that dictionary inside `prob01()` and return it so it can be tested.

### Function Signature

```python
def prob01():
    pass
```

### Examples

**Example 1:**
```
Input:  hollywood_stars = prob01()
        list(hollywood_stars.keys())
Output: ['Kevin Bacon', 'Meryl Streep', 'Idris Elba', 'Laverne Cox', 'Sofia Vergara']
```

**Example 2:**
```
Input:  hollywood_stars = prob01()
        list(hollywood_stars.values())
Output: [['Laverne Cox', 'Sofia Vergara'], ['Idris Elba', 'Sofia Vergara'],
         ['Meryl Streep', 'Laverne Cox'], ['Kevin Bacon', 'Idris Elba'],
         ['Kevin Bacon', 'Meryl Streep']]
```

**Example 3:**
```
Input:  hollywood_stars = prob01()
        hollywood_stars["Kevin Bacon"]
Output: ['Laverne Cox', 'Sofia Vergara']
```

---

## Problem 2: The Feeling is Mutual

**Difficulty:** Medium

### Description

You are given an insider look into Hollywood gossip with an adjacency matrix `celebrities` where each node labeled `0` to `n` represents a celebrity. `celebrities[i][j] = 1` indicates that celebrity `i` likes celebrity `j`, and `celebrities[i][j] = 0` indicates that celebrity `i` dislikes or doesn't know celebrity `j`.

Return `True` if all relationships between celebrities are mutual and `False` otherwise.

**A relationship is mutual if:**
- For any celebrity `i` that likes celebrity `j`, celebrity `j` also likes celebrity `i`

### Function Signature

```python
def prob02(celebrities):
    pass
```

### Examples

**Example 1:**
```
Input:  celebrities = [
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 1, 0]]
Output: True
```

**Example 2:**
```
Input:  celebrities = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]
Output: False
```

---

## Problem 3: Closest Friends

**Difficulty:** Easy

### Description

You are a talented actor looking for your next big movie and want to leverage your connections to see if there are any good roles available. To increase your chances, you want to ask your closest friends first.

You have a 2D list `contacts` where `contacts[i] = [celebrity_a, celebrity_b]` indicates there is a mutual relationship (undirected edge) between `celebrity_a` and `celebrity_b`. Given a celebrity `celeb`, return a list of that celebrity's closest friends.

`celebrity_b` is a close friend of `celebrity_a` if they are neighbors in the graph.

### Function Signature

```python
def prob03(contacts, celeb):
    pass
```

### Examples

**Example 1:**
```
Input:  contacts = [["Lupita Nyong'o", "Jordan Peele"], ["Meryl Streep", "Jordan Peele"],
                    ["Meryl Streep", "Lupita Nyong'o"], ["Greta Gerwig", "Meryl Streep"],
                    ["Ali Wong", "Greta Gerwig"]]
        celeb = "Lupita Nyong'o"
Output: ['Jordan Peele', 'Meryl Streep']
```

**Example 2:**
```
Input:  contacts = [["Lupita Nyong'o", "Jordan Peele"], ["Meryl Streep", "Jordan Peele"],
                    ["Meryl Streep", "Lupita Nyong'o"], ["Greta Gerwig", "Meryl Streep"],
                    ["Ali Wong", "Greta Gerwig"]]
        celeb = "Greta Gerwig"
Output: ['Meryl Streep', 'Ali Wong']
```

---

## Problem 4: Network Lookup

**Difficulty:** Medium

### Description

You work for a talent agency and have a 2D list `clients` where `clients[i] = [celebrity_a, celebrity_b]` indicates that `celebrity_a` and `celebrity_b` have worked with each other. You want a more efficient lookup system by transforming `clients` into an equivalent adjacency matrix.

Given `clients`:

1. Create a map of each unique celebrity in `clients` to an integer ID with values `0` through `n`.
2. Using the celebrities' IDs, create an adjacency matrix where `matrix[i][j] = 1` indicates that the celebrity with ID `i` has worked with the celebrity with ID `j`. Otherwise `matrix[i][j]` should be `0`.

Return both the dictionary mapping celebrities to their ID and the adjacency matrix.

### Function Signature

```python
def prob04(clients):
    pass
```

### Examples

**Example 1:**
```
Input:  clients = [
            ["Yalitza Aparicio", "Julio Torres"],
            ["Julio Torres", "Fred Armisen"],
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"],
            ["Ali Wong", "Bowen Yang"]]
Output: id_map = {
            'Fred Armisen': 0,
            'Yalitza Aparicio': 1,
            'Margaret Cho': 2,
            'Bowen Yang': 3,
            'Ali Wong': 4,
            'Julio Torres': 5
        }
        adj_matrix = [
            [0, 0, 0, 0, 1, 1],  # Fred Armisen
            [0, 0, 0, 0, 0, 1],  # Yalitza Aparicio
            [0, 0, 0, 1, 1, 0],  # Margaret Cho
            [0, 0, 1, 0, 1, 1],  # Bowen Yang
            [1, 0, 1, 1, 0, 0],  # Ali Wong
            [1, 1, 0, 1, 0, 0]   # Julio Torres
        ]
```

### Constraints

- The order in which you assign IDs — and consequently your adjacency matrix — may look different.

---

## Problem 5: Secret Celebrity

**Difficulty:** Unknown

### Description

_Problem text not yet provided — paste the full description to fill this in._

---

## Problem 6: Casting Call Search

**Difficulty:** Unknown

### Description

_Problem text not yet provided — paste the full description to fill this in._

---

## Problem 7: Casting Call Search II

**Difficulty:** Medium

### Description

You are a casting agent for a major Hollywood production and the director has a certain celebrity in mind for the lead role. You have an adjacency matrix `celebs` where `celebs[i][j] = 1` means that celebrity `i` has a connection with celebrity `j`, and `celebs[i][j] = 0` means they don't. Connections are directed, meaning that `celebs[i][j] = 1` does not automatically mean `celebs[j][i] = 1`.

Given a celebrity you know `start_celeb` and the celebrity the director wants to hire `target_celeb`, use Depth First Search to return `True` if you can find a path of connections from `start_celeb` to `target_celeb`. Otherwise return `False`.

### Function Signature

```python
def prob07(celebs, start_celeb, target_celeb):
    pass
```

### Examples

**Example 1:**
```
Input:  celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0],  # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0],  # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0],  # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]]  # Celeb 7
        start_celeb = 0
        target_celeb = 6
Output: True
```

**Example 2:**
```
Input:  celebs = [
            [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 0
            [0, 1, 1, 0, 0, 0, 0, 0],  # Celeb 1
            [0, 0, 0, 1, 0, 1, 0, 0],  # Celeb 2
            [0, 0, 0, 0, 1, 0, 1, 0],  # Celeb 3
            [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 4
            [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 5
            [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 6
            [0, 0, 0, 0, 1, 0, 1, 0]]  # Celeb 7
        start_celeb = 3
        target_celeb = 5
Output: False
```

---

## Problem 8: Copying Seating Arrangements

**Difficulty:** Hard

### Description

You are organizing the seating arrangement for a big awards ceremony and want to make a copy for your assistant. The seating arrangement is stored in a graph where each `Node` value `val` is the name of a celebrity guest at the ceremony, and its list `neighbors` holds all the guests sitting in seats adjacent to that celebrity.

Given a reference to a `Node` in the original seating arrangement `seat`, make a deep copy (clone) of the seating arrangement. Return the copy of the given node.

`compare_graphs()` is provided to help with testing. Pass in the given node `seat` and the copy your function returns — it returns `True` if the two graphs are clones of each other, `False` otherwise.

### Starter Code

```python
class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Function to test if two seating arrangements (graphs) are identical
def compare_graphs(node1, node2, visited=None):
    if visited is None:
        visited = set()

    if node1.val != node2.val:
        return False

    visited.add(node1)

    if len(node1.neighbors) != len(node2.neighbors):
        return False

    for n1, n2 in zip(node1.neighbors, node2.neighbors):
        if n1 not in visited and not compare_graphs(n1, n2, visited):
            return False

    return True
```

### Function Signature

```python
def prob08(seat):
    pass
```

### Examples

**Example 1:**
```
Input:  lily = Node("Lily Gladstone")
        mark = Node("Mark Ruffalo")
        cillian = Node("Cillian Murphy")
        danielle = Node("Danielle Brooks")
        lily.neighbors.extend([mark, danielle])
        mark.neighbors.extend([lily, cillian])
        cillian.neighbors.extend([danielle, mark])
        danielle.neighbors.extend([lily, cillian])

        copy = prob08(lily)
        compare_graphs(lily, copy)
Output: True
```
