class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Store a list of evaluated numbers
        checkednumbers = []
        for i in nums:
            # O(n) speed
            if i in checkednumbers:
                return True
            checkednumbers.append(i)
        return False