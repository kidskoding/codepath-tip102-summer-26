'''
    Input: A string to check for symmetry
    Output: A boolean that determines whether the input string is symmetrical or not
    Edge Case (to clarify in interview): Numbers???

    1. Lowercasing the input string title and then removing all instances of punctuation and spaces
    2. Initialize left and right pointers at the left and right ends of the string
    3. Go through the input string and check the ends using the left and right pointers and continue to do so as long as the left pointer doesn't overlap (go past) the right pointer
        4. Check if the character at the left pointer and right pointer are equal. If not, return False immediately because it can't be symmetric otherwise
        5. Move left pointer forward one and right pointer back one
    6. Return True at the end, indicating that left and right pointers have overlapped and characters on both ends have been equal

    Time: O(n)
    Space: O(1)
'''

def prob03(title: str) -> bool:
    import re

    title = title.lower()
    title = re.sub('[^a-zA-Z0-9]', '', title)

    left, right = 0, len(title) - 1
    while left < right:
        if title[left] != title[right]:
            return False

        left += 1
        right -= 1

    return True
