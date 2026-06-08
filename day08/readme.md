# Day 8: Subarray Product Less Than K

## 🔗 Question Link
You can find the problem statement and test your solution directly on LeetCode: [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

---

## 💡 Approach & Algorithm

The problem asks for **contiguous subarrays**, and all elements in `nums` are strictly positive ($\ge 1$). This means that multiplying by a new element will always increase (or maintain) the product, while dividing out an element will decrease it. Because of this monotonic behavior, we can use an optimized **Sliding Window (Two-Pointer)** technique instead of a brute-force $\mathcal{O}(N^2)$ approach.

### Step-by-Step Breakdown

1. **Edge Case Handling:** Since $nums[i] \ge 1$, the smallest possible product of a non-empty subarray is `1`. If $k \le 1$, it is mathematically impossible to have a product *strictly less than* $k$. In this case, we immediately return `0`.

2. **Expanding the Window:**
   We iterate through the array using a right pointer (`right`). For each element, we multiply it into our running `current_product`.

3. **Shrinking the Window:**
   If `current_product` becomes greater than or equal to `k`, the window is no longer valid. We contract the window from the left by dividing `current_product` by `nums[left]` and incrementing the `left` pointer until `current_product < k` again.

4. **Counting Subarrays (The Math Trick):**
   For any valid window bounded between `left` and `right`, the number of **new valid contiguous subarrays** ending exactly at index `right` is equal to the size of the window:
   $$\text{window\_size} = \text{right} - \text{left} + 1$$

### Visual Walkthrough
For `nums = [10, 5, 2]`, `k = 100`:
* `right = 0` (val: 10): Product = 10. Valid window `[10]`. New subarrays: `[10]` (+1)
* `right = 1` (val: 5): Product = 50. Valid window `[10, 5]`. New subarrays: `[5]`, `[10, 5]` (+2)
* `right = 2` (val: 2): Product = 100 ($\ge k$). Shrink left! Divide by 10, `left` moves to 1. Product = 10. Valid window `[5, 2]`. New subarrays: `[2]`, `[5, 2]` (+2)

---

## 📊 Complexity Analysis

| Complexity | Scale | Reason |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ | Each element is processed at most twice: once when expanded by the `right` pointer, and at most once when compressed by the `left` pointer. |
| **Space Complexity**| $\mathcal{O}(1)$ | The algorithm operates completely in-place using only a few primitive integer trackers (`left`, `right`, `current_product`, `total_count`). |
