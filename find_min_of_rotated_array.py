# We'll have the find the minimum element in a rotated sorted array.
# The array is rotated at some pivot unknown to you beforehand.
# For example, the array [3,4,5,1,2] might be rotated at index 3 and becomes [1,2,3,4,5].
# The array is guaranteed to be sorted in ascending order before rotation.

# The problem can be solved in two ways:
# 1. Linear Search
# 2. Binary Search

# Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)
import math
def find_min(arr):
    min_el = math.inf
    for i in arr:
        if i < min_el:
            min_el=i
        
    return(min_el)

# Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_min_bin(arr):
    left=0
    right =len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]<arr[right]:
            right=mid
        else:
            left=mid+1
    return nums[left]

arr=[5,6,7,8,9,1,2,3,4]
