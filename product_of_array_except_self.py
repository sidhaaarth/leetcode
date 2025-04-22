# Products of Array Except Self
# Solved 
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.


import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_array=[]
        for i,value in enumerate(nums):
            nums_ = nums[:i] + nums[i+1:]
            prod_array.append(math.prod(nums_))
            
        return prod_array