'''
    Input: A string, called posts, that contains the necessary post metadata
    Output: A boolean that determines whether or not the input posts string was formatted properly

    1. Create a dictionary that will contain the valid pairings of open (values) and closed (keys) brackets of all types (square, curly, etc.)
    2. Use a stack to track the top most character visited in the posts input string
    3. Loop through the characters in the input posts string
        4. Check for dictionary membership (keys)
        5. Check if we have elements in our stack (cannot get elements from a stack if empty). If not, return False immediately
        6. Pop the topmost element from stack and check if there is a valid open and close bracket pair. If not, return False immediately because a valid pairing of brackets is impossible
    7. Return True if stack is empty, otherwise return False

    Time: O(n)
    Space: O(n)
'''

def prob01(posts: str) -> bool:
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    opening = set(brackets_dict.values())
    stack = []

    for ch in posts:
        if ch in opening:
            stack.append(ch)          # push opening brackets so they can be matched
        elif ch in brackets_dict:
            if not stack:
                return False

            top = stack.pop()
            if top != brackets_dict[ch]:
                return False

    return not stack
