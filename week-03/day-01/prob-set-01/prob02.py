# Input: A list of strings represented as a queue
# Output: A list of strings that are a reverse of the original input list via a stack
# 
# 1. Need a Stack - to get the top most string from the comments input list
# 2. Loop through our comments input list
#   3. Push the string onto the stack
# 4. Modify the input comments list of strings to be in the reversed order using the stack
# 5. Return the modified input comments list
# 
# Time: O(n)
# Space: O(n)

def prob02(comments: list[str]) -> list[str]:
    stack = []

    for comment in comments:
        stack.append(comment)

    i = 0
    while stack and i < len(comments):
        comments[i] = stack.pop()
        i += 1

    return comments
