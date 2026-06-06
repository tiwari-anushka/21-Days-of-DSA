# Day 6: 3Sum

## 🔗 Links & Problem Statement
* **Problem Link:** [3Sum on LeetCode](https://leetcode.com/problems/3sum/)

### Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

---

## 💡 Approach
The naive approach uses three nested loops, resulting in an inefficient $O(N^3)$ time complexity. To optimize this to $O(N^2)$, we can use a **Sorting + Two-Pointer** approach.

By sorting the array first:
1.  We can fix one element ($nums[i]$) and use two pointers (`left` and `right`) to find the other two elements in linear time.
2.  We can easily skip adjacent identical elements to guarantee that our final results contain only unique triplets without needing a costly global look-up step.

---

## 🛠️ Algorithm

1.  **Sort the input array** in ascending order.
2.  **Iterate through the array** with a loop variable `i` tracking the first element:
    * *Optimization:* If the current element $nums[i] > 0$, break the loop immediately (since the array is sorted, no subsequent positive numbers can sum to zero).
    * *Duplicate handling:* If `i > 0` and $nums[i] == nums[i-1]$, `continue` to skip it.
3.  **Initialize Two Pointers** for every valid `i`:
    * `left = i + 1`
    * `right = len(nums) - 1`
4.  **Run a loop while `left < right`**:
    * Calculate $current\_sum = nums[i] + nums[left] + nums[right]$.
    * **Case 1: $current\_sum == 0$**
        * Save the triplet `[nums[i], nums[left], nums[right]]` to the results list.
        * Proactively skip duplicate values for both pointers:
            * While `left < right` and $nums[left] == nums[left + 1]$, increment `left`.
            * While `left < right` and $nums[right] == nums[right - 1]$, decrement `right`.
        * Move both pointers inward (`left += 1`, `right -= 1`).
    * **Case 2: $current\_sum < 0$**
        * The sum is too small. Move the `left` pointer to the right (`left += 1`) to get a larger value.
    * **Case 3: $current\_sum > 0$**
        * The sum is too large. Move the `right` pointer to the left (`right -= 1`) to get a smaller value.

---

## 📊 Complexities

* **Time Complexity:** $O(N^2)$
    * Sorting the array takes $O(N \log N)$.
    * The outer loop runs $N$ times, and the inner two-pointer scan processes the rest of the array in $O(N)$ time per iteration. 
    * $O(N \log N) + O(N^2) = O(N^2)$.
* **Space Complexity:** $O(1)$ to $O(N)$
    * The space complexity depends entirely on the implementation details of the sorting algorithm used by the underlying language platform, as no additional data structures are utilized to track elements.
