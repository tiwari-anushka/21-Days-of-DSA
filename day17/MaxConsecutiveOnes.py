class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            # If we encounter a 0, increase our zero counter
            if nums[right] == 0:
                zero_count += 1
            
            # If the number of zeros in the current window exceeds k,
            # shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Calculate the maximum window size seen so far
            max_length = max(max_length, right - left + 1)
            
        return max_length
