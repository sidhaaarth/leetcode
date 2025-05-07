class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        for i in range(len(numbers)):
            if target-numbers[i] in numbers:
                diff_index = numbers.index(target-numbers[i])
                arr = [i+1,diff_index+1]
                return arr