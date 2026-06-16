class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # dict to store character frequencies
        left = 0
        max_freq = 0
        max_length = 0
        
        for right in range(len(s)):
            # Add the current character to our frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Update the maximum frequency of any character in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # Current window size is (right - left + 1)
            # If the operations needed exceed k, shrink the window from the left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # The window size is always valid or optimized at this point
            max_length = max(max_length, right - left + 1)
            
        return max_length
