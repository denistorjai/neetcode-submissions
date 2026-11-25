class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        CheckedNumbers = {}

        for i,v in enumerate(nums):
            tocheck = target - v
            if tocheck in CheckedNumbers:
                return [CheckedNumbers[tocheck],i]
            CheckedNumbers[v] = i
