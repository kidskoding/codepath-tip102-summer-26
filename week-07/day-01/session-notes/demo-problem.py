'''
    EXAMPLE PROBLEM

    """
    UNDERSTAND
    Input: sorted array, target value
    Output: array of [leftmost, rightmost] occurrence of that target value
     - [-1,-1]
    
    MATCH:
    -  binary search twice 
    - once to find left, another to find right
    
    PLAN
    - find_left : dont stop after you find it, keep going left
    - find_right : dont stop after you find it, keep going right
    """
'''

def find_left(nums, target):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:

        mid = (left + right) // 2
    
        if nums[mid] == target:
            index = mid
            right = mid-1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
        
    return index

def find_right(nums, target):
    left, right = 0, len(nums) - 1
    index = -1

    while left <= right:

        mid = (left + right) // 2
    
        if nums[mid] == target:
            index = mid
            left = mid+1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
        
    return index

nums = [1,3,5,5,5,7,9,11]
target = 3

print(find_left(nums, target), find_right(nums, target))
