# Day 7: 3Sum Closest

## 🔗 Links
- **Problem Link:** [LeetCode - 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

---

## 📝 Problem Statement
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*. You may assume that each input would have exactly one solution.

### Example 1:
> **Input:** `nums = [-1, 2, 1, -4]`, `target = 1`  
> **Output:** `2`  
> **Explanation:** The sum that is closest to the target is 2. (`-1 + 2 + 1 = 2`).

### Example 2:
> **Input:** `nums = [0, 0, 0]`, `target = 1`  
> **Output:** `0`  
> **Explanation:** The sum that is closest to the target is 0. (`0 + 0 + 0 = 0`).

---

## 💡 Approach & Algorithm
The problem can be efficiently solved using a **Sorting** and **Two-Pointer** technique rather than a brute-force $O(n^3)$ solution.

1. **Sort the Array:** Sorting allows us to strategically move pointers to increase or decrease our current sum relative to the target.
2. **Iterate with a Fixed Element:** Loop through the array using a pointer `i` as the first element of our triplet. 
3. **Initialize Two Pointers:** For every fixed `i`, place a `left` pointer at `i + 1` and a `right` pointer at the end of the array (`len(nums) - 1`).
4. **Evaluate and Update:** - Calculate the `current_sum = nums[i] + nums[left] + nums[right]`.
   - If `current_sum` equals the `target`, return it immediately as it's a perfect match.
   - Track the closest sum by storing the absolute difference between the `current_sum` and the `target` in a hash map/dictionary.
   - **Pointer Shifting:** If `current_sum < target`, increment `left` to look for a larger sum. Otherwise, decrement `right` to look for a smaller sum.
5. **Result:** Once all pairs are evaluated, find the key in the dictionary that corresponds to the minimum absolute difference.

---

## 📊 Complexities

- **Time Complexity:** $O(n^2)$  
  - **Sorting:** Sorting the array takes $O(n \log n)$ time.  
  - **Two-Pointer Traversal:** The outer loop runs $n$ times, and the inner `while` loop moves the two pointers toward each other, taking $O(n)$ steps per iteration. This results in an $O(n^2)$ traversal.
  - **Overall Time:** Since $O(n^2)$ grows faster than $O(n \log n)$, the final time complexity is dominated by **$O(n^2)$**.

- **Space Complexity:** $O(n)$  
  - **Hash Map Storage:** Space is utilized by the `ans` dictionary to store the calculated sums and their absolute differences from the target, which can hold up to $O(n^2)$ unique sums in the worst-case scenario.
  - **Sorting Auxiliary Space:** Sorting also requires auxiliary space (up to $O(n)$ depending on the programming language's internal sorting implementation, like Python's Timsort).
