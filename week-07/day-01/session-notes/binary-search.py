# Binary Search Algorithm
# Time: O(log n)
# Space: O(1)

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

nums, target = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 2
target = 5

print(binary_search(nums, target))