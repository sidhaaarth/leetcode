
# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].


# Recommended Time & Space Complexity
# You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if i>0 and a == nums[i-1]:      # We'd now have to check for duplicates and negate them. Consider a list [1,1,2,3,-4,5] where the possible triplets is [1,3,-4]. But since there are two 1's, we dont want them to duplicate and create two diff triplets. Hence we create a condition where in if the i is not zero and current i value is equal to the previous one in a sorted array we continue the loop
            continue
        l=i+1                           # Here we create pointers with next_element_to_i in the example list taking the 'l' and nth_element taking the 'r' value
        r=len(nums)-1
        while l<r:                      # This is the base condition we're setting, as long as l is less than r, we have the window not making duplicates
            threeSum = a+nums[l]+nums[r]
            if threeSum >0:             # if the sum is greater than zero, we move left in the sorted array and vice versa
                r-=1
            elif threeSum<0:
                l+=1
            else:                       # Here comes the tricky part, once we append the tuple to the result_list,we'd have to move further to find other possible pairs. That works by incrementing 'l' and decrementing 'r'. We dont just increment or decrement either because for a constant 'a', changing only l or r would not sum to 0, and if it did, it is a duplicate
                res.append([a,nums[l],nums[r]])
                l+=1
                r-=1
                while nums[l]==nums[l-1] and l<r:      # We then implement the same logic we did for i to negate duplicates
                    l+=1
    return res