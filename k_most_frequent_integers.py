# Top K Frequent Elements
# Solved 
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.


from collections import OrderedDict
import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dict and add elements from the list and update the values based on the frequency
        count ={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        
        # To reverse sort the dict based on the values
        keys = list(count.keys())
        values = list(count.values())

        # argsort() returns a list of index-es based on the sorted arguments (values in this case)
        # For example, if values = [30, 10, 50], then np.argsort(values) returns [1, 0, 2] 
        reverse_sorted_value_index = np.argsort(values)[::-1]
        reverse_sorted_dict = {keys[i]: values[i] for i in reverse_sorted_value_index}
        
        # then we initiate an array and loop the original reverse_sorted_dict until the range(k) and append it to the array and return it
        k_elements = []
        dict_keys = list(reverse_sorted_dict.keys())
        for i in range(k):
            k_elements.append(dict_keys[i])    
        return k_elements