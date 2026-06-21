class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        # Phase 1: Cyclic Sort
        while i < n:
            correct_idx = nums[i]
            # If the current number is less than n and not at its correct index, swap it
            if nums[i] < n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
                
        # Phase 2: Find the missing number
        for i in range(n):
            if nums[i] != i:
                return i
                
        # If all numbers from 0 to n-1 are in their correct spots, n is missing
        return n
        
