'''
    INPUT: A list of tuples containing the priority and type of music
    OUTPUT: A list of strings containing ordering the type of music by its priority

    1. Sort the changes list in reverse by priority, where the highest priority comes first in the list. This preserves the ordering by priority
    2. Create a queue that be able to process the type of music along with its priority in the order that it was given
    3. Create a resulting list that will be able to add the specific type of music in the descending order based on priority
    4. While loop through the queue until no more elements are present
        5. Pop the rightmost element from the queue and extract the music type. Add this to the resulting list
    6. Return the resulting list

    Time: O(n) - worst case scenario we loop through all elements n possible times
    Space: O(n) - because we store a max of n elements into the queue
'''

from collections import deque

def prob02(requests: list[str]) -> list[str]:
    requests = sorted(requests)
    queue = deque(requests)
    res = []

    while queue:
        elem = queue.pop()
        res.append(elem[1])

    return res
