class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is already in the set, 
            # shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length
