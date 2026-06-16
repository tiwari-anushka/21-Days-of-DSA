from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        left = 0
        max_fruits = 0
        
        # 'right' expands the sliding window
        for right in range(len(fruits)):
            basket[fruits[right]] += 1
            
            # If we have more than 2 types of fruit, shrink the window from the left
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            # Calculate the current window size and update max_fruits
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits
            
