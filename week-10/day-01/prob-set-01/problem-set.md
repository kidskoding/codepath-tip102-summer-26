# Problem Set #1: Graphs — Week 10, Day 1

---

## Problem 1: Graphing Flights

**Difficulty:** Easy

### Description

The graph below represents the flights offered by CodePath Airlines. Each node (vertex) is an airport (JFK — New York City, LAX — Los Angeles, DFW — Dallas Fort Worth, ATL — Atlanta), and an edge between two vertices means CodePath Airlines offers flights between those airports.

```
JFK ----- LAX
 |
 |
DFW ----- ATL
```

Represent this undirected graph as an adjacency dictionary where each node's value is a string with the airport's name (ex. `"JFK"`).

The original problem asks for a module-level variable `flights`. Build that dictionary inside `prob01()` and return it so it can be tested.

### Function Signature

```python
def prob01():
    pass
```

### Examples

**Example 1:**
```
Input:  flights = prob01()
        list(flights.keys())
Output: ['JFK', 'LAX', 'DFW', 'ATL']
```

**Example 2:**
```
Input:  flights = prob01()
        list(flights.values())
Output: [['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
```

**Example 3:**
```
Input:  flights = prob01()
        flights["JFK"]
Output: ['LAX', 'DFW']
```

---

## Problem 2: There and Back

**Difficulty:** Medium

### Description

As a flight coordinator for CodePath Airlines, you have a 0-indexed adjacency list `flights` with `n` nodes where each node represents the ID of a different destination, and `flights[i]` is an integer array indicating there is a flight from destination `i` to each destination in `flights[i]`.

Return `True` if for every flight from a destination `i` to a destination `j` there also exists a flight from destination `j` to destination `i`. Return `False` otherwise.

### Function Signature

```python
def prob02(flights):
    pass
```

### Examples

**Example 1:**
```
Input:  flights = [[1, 2], [0], [0, 3], [2]]
Output: True
```

**Example 2:**
```
Input:  flights = [[1, 2], [], [0], [2]]
Output: False
```

---

## Problem 3: Finding Direct Flights

**Difficulty:** Easy

### Description

You are given an adjacency matrix `flights` of size `n x n` where each of the `n` nodes represents a distinct destination. `flights[i][j] = 1` indicates there is a flight from destination `i` to destination `j`, and `flights[i][j] = 0` indicates no such flight exists.

Given `flights` and an integer `source` representing the destination a customer is flying out of, return a list of all destinations the customer can reach from `source` on a direct flight. You may return the destinations in any order.

A customer can reach a destination on a direct flight if that destination is a neighbor of `source`.

### Function Signature

```python
def prob03(flights, source):
    pass
```

### Examples

**Example 1:**
```
Input:  flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]
        source = 2
Output: [0, 1, 3]
```

**Example 2:**
```
Input:  flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]
        source = 3
Output: []
```

---

## Problem 4: Converting Flight Representations

**Difficulty:** Medium

### Description

Given a list of edges `flights` where `flights[i] = [a, b]` denotes that there exists a bidirectional flight (incoming and outgoing) from city `a` to city `b`, return an adjacency dictionary `adj_dict` representing the same flights graph, where `adj_dict[a]` is a list denoting there is a flight from city `a` to each city in `adj_dict[a]`.

### Function Signature

```python
def prob04(flights):
    pass
```

### Examples

**Example 1:**
```
Input:  flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'],
                   ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
Output: {
            'Cape Town': ['Addis Ababa', 'Cairo'],
            'Addis Ababa': ['Cape Town', 'Lagos'],
            'Lagos': ['Cairo', 'Addis Ababa'],
            'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
            'Nairobi': ['Cairo']
        }
```

---

## Problem 5: Find Center of Airport

**Difficulty:** Easy

### Description

You are a pilot navigating a new airport and have a map of the airport represented as an undirected star graph with `n` nodes, where each node represents a terminal labeled from `1` to `n`. You want to find the center terminal where the pilots' lounge is located.

Given a 2D integer array `terminals` where each `terminals[i] = [u, v]` indicates there is a path (edge) between terminal `u` and `v`, return the center of the given airport.

A star graph is a graph where there is one center node and exactly `n - 1` edges connecting the center node to every other node.

### Function Signature

```python
def prob05(terminals):
    pass
```

### Examples

**Example 1:**
```
Input:  terminals = [[1, 2], [2, 3], [4, 2]]
Output: 2
```

**Example 2:**
```
Input:  terminals = [[1, 2], [5, 1], [1, 3], [1, 4]]
Output: 1
```

---

## Problem 6: Finding All Reachable Destinations

**Difficulty:** Medium

### Description

You are a travel coordinator for CodePath Airlines helping a customer find all possible destinations reachable from a starting airport. The flight connections are represented as an adjacency dictionary `flights`, where each key is a destination and the corresponding value is a list of other destinations reachable through a direct flight.

Given a starting location `start`, return a list of all destinations reachable from `start` either through a direct flight or through connecting flights with layovers. The list should be in ascending order by number of layovers required (breadth first).

### Function Signature

```python
def prob06(flights, start):
    pass
```

### Examples

**Example 1:**
```
Input:  flights = {
            "Tokyo": ["Sydney"],
            "Sydney": ["Tokyo", "Beijing"],
            "Beijing": ["Mexico City", "Helsinki"],
            "Helsinki": ["Cairo", "New York"],
            "Cairo": ["Helsinki", "Reykjavik"],
            "Reykjavik": ["Cairo", "New York"],
            "Mexico City": ["Sydney"],
            "New York": []
        }
        start = "Beijing"
Output: ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 'Reykjavik']
```

**Example 2:**
```
Input:  flights = {
            "Tokyo": ["Sydney"],
            "Sydney": ["Tokyo", "Beijing"],
            "Beijing": ["Mexico City", "Helsinki"],
            "Helsinki": ["Cairo", "New York"],
            "Cairo": ["Helsinki", "Reykjavik"],
            "Reykjavik": ["Cairo", "New York"],
            "Mexico City": ["Sydney"],
            "New York": []
        }
        start = "Helsinki"
Output: ['Helsinki', 'Cairo', 'New York', 'Reykjavik']
```

---

## Problem 7: Finding All Reachable Destinations II

**Difficulty:** Medium

### Description

Same setup as Problem 6, but this time use Depth First Search (DFS) to return a list of all destinations that can be reached from `start`. The list should include both direct and connecting flights, ordered based on the order in which airports are visited in DFS.

### Function Signature

```python
def prob07(flights, start):
    pass
```

### Examples

**Example 1:**
```
Input:  flights = {
            "Tokyo": ["Sydney"],
            "Sydney": ["Tokyo", "Beijing"],
            "Beijing": ["Mexico City", "Helsinki"],
            "Helsinki": ["Cairo", "New York"],
            "Cairo": ["Helsinki", "Reykjavik"],
            "Reykjavik": ["Cairo", "New York"],
            "Mexico City": ["Sydney"]
        }
        start = "Beijing"
Output: ['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 'New York']
```

**Example 2:**
```
Input:  flights = {
            "Tokyo": ["Sydney"],
            "Sydney": ["Tokyo", "Beijing"],
            "Beijing": ["Mexico City", "Helsinki"],
            "Helsinki": ["Cairo", "New York"],
            "Cairo": ["Helsinki", "Reykjavik"],
            "Reykjavik": ["Cairo", "New York"],
            "Mexico City": ["Sydney"]
        }
        start = "Helsinki"
Output: ['Helsinki', 'Cairo', 'Reykjavik', 'New York']
```

### Constraints

- `"New York"` has no outgoing flights and is not a key in `flights` — handle missing keys.

---

## Problem 8: Find Itinerary

**Difficulty:** Medium

### Description

You are a traveler about to embark on a multi-leg journey. You have all your boarding passes, but their order has gotten mixed up. You want to organize them in the order you will use them, from your first flight all the way to the last flight that brings you to your final destination.

Given a list of edges `boarding_passes` where each element `boarding_passes[i] = (departure_airport, arrival_airport)` represents a flight from `departure_airport` to `arrival_airport`, return a list with the itinerary listing the airports you pass through in the order you visit them.

Assume that a departure is scheduled from every airport except the final destination, and each airport is visited only once (there are no cycles in the route).

### Function Signature

```python
def prob08(boarding_passes):
    pass
```

### Examples

**Example 1:**
```
Input:  boarding_passes = [("JFK", "ATL"), ("SFO", "JFK"), ("ATL", "ORD"), ("LAX", "SFO")]
Output: ['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
```

**Example 2:**
```
Input:  boarding_passes = [("LAX", "DXB"), ("DFW", "JFK"), ("LHR", "DFW"), ("JFK", "LAX")]
Output: ['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
```
