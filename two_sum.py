# Two Sum
# Solved 
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        ## IMPORTANT: Never iterate and operate on the same array
        
        # Enumerating provides the index and value at the same time
        for i, element in enumerate(nums):
            diff = target - element

            # Basically check if the diff element is already there on the dict, if yes the diff element and the current element are the pair that adds up to targer. 
            # So we can return the num_dict[diff] which gives its index and 'i' which gives the current element's index.
            if diff in num_dict:
                return [num_dict[diff], i]
            
            # Pretty starightforward, if the diff is not already present you add the current element to the num_dict
            # Assume nums = [3,4,5,6], target = 7, for i=0, element=3 => diff=4... We here dont add the diff rather the current_element to the num_dict because we need to find the current element's complement
            # So when i=1, element=4, the diff becomes 3 which would be present in the num_dict because we had added it in the last iteration, and goes into the if condition, hence returns [0,1] => num_dict[3] (which is 0) and the then 'i' which would be 1
            num_dict[element] = i
        return []


        