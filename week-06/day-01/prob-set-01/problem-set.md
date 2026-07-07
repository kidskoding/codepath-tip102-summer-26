# Problem Set: Linked Lists — Week 6, Day 1

---

## Problem 1: Building a Playlist

**Difficulty:** Easy

### Description

The assignment statement to the `top_hits_2010s` variable below creates the linked list `Uptown Funk -> Party Rock Anthem -> Bad Romance`. Break apart the assignment statement into multiple lines with one call to the `Node` constructor per line to recreate the list.

### Starter Code

```python
class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()

top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))
```

### Examples

**Example 1:**
```
Input:  print_linked_list(top_hits_2010s)
Output: Uptown Funk -> Party Rock Anthem -> Bad Romance
```

---

## Problem 2: Top Artists

**Difficulty:** Easy

### Description

Given the head of a linked list `playlist`, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Starter Code

```python
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()
```

### Function Signature

```python
def get_artist_frequency(playlist):
    pass
```

### Examples

**Example 1:**
```
Input:
playlist = SongNode("Saturn", "SZA",
                SongNode("Who", "Jimin",
                        SongNode("Espresso", "Sabrina Carpenter",
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)

Output: { "SZA": 2, "Jimin": 1, "Sabrina Carpenter": 1 }
```

---

## Problem 3: Glitching Out

**Difficulty:** Medium

### Description

The following code attempts to remove the first node with a given song from a singly linked list with head `playlist_head` but it contains a bug!

**Step 1:** Copy this code into your IDE.

**Step 2:** Create your own test cases to run the code against, and use print statements and the stack trace to identify and fix the bug so that the function correctly removes a node by value from the list.

**Step 3:** Evaluate the time and space complexity of the fixed solution. Define your variables and provide a rationale for why you believe the solution has the stated time and space complexity.

### Starter Code

```python
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current = current.next.next
            return playlist_head
        current = current.next

    return playlist_head
```

### Examples

**Example 1:**
```
Input:
playlist = SongNode("SOS", "ABBA",
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

print_linked_list(remove_song(playlist, "Dreams"))

Output: ('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Lovely Day', 'Bill Withers')
```

---

## Problem 4: On Repeat

**Difficulty:** Medium

### Description

A variation of the two-pointer technique introduced in previous units is to have a slow and a fast pointer that increment at different rates.

We would like to check whether our playlist loops or not. Given the head of a linked list `playlist_head`, return `True` if the playlist has a cycle in it and `False` otherwise. A linked list has a cycle if at some point in the list, the node's `next` pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Starter Code

```python
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next
```

### Function Signature

```python
def on_repeat(playlist_head):
    pass
```

### Examples

**Example 1:**
```
Input:
Linked list of four songs, with fourth song pointing back to second song

song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))

Output: True
```

---

## Problem 5: Looped

**Difficulty:** Medium

### Description

Given the head of a linked list `playlist_head` that may contain a cycle, use the fast and slow pointer method to return the length of the cycle. If the list does not contain a cycle, return 0.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Starter Code

```python
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()
```

### Function Signature

```python
def loop_length(playlist_head):
    pass
```

### Examples

**Example 1:**
```
Input:
Linked list of four songs, with fourth song pointing back to second song

song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))

Output: 3
```

---

## Problem 6: Volume Control

**Difficulty:** Medium

### Description

You are working as an engineer normalizing volume levels on songs. Given the head of a singly linked list with integer values `song_audio` representing volume levels at different points in a song, return the number of critical points. A critical point is a local minima or maxima.

**A solution is considered valid if:**
- The head and tail nodes are not considered critical points.
- A node is a local minima if both the next and previous elements are greater than the current element.
- A node is a local maxima if both the next and previous elements are less than the current element.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

### Starter Code

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
```

### Function Signature

```python
def count_critical_points(song_audio):
    pass
```

### Examples

**Example 1:**
```
Input:
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))

Output: 3
```

Explanation: There are three critical points:
- The third node is a local minima because 1 is less than 3 and 2.
- The fifth node is a local maxima because 5 is greater than 2 and 1.
- The sixth node is a local minima because 1 is less than 5 and 2.

---
