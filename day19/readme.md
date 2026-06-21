# Day 19: Find All Numbers Disappeared in an Array

## 🔗 Problem Link
You can find the problem description and submit your solution on [LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/).

---

## 📝 Problem Description

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.

### Example 1
> **Input:** `nums = [4, 3, 2, 7, 8, 2, 3, 1]`  
> **Output:** `[5, 6]`

### Example 2
> **Input:** `nums = [1, 1]`  
> **Output:** `[2]`

---

## 💡 Approach: Cyclic Sort

Since the elements in the array are expected to be in the range `[1, n]`, each number $x$ has a unique "home" index, which is $x - 1$. For example, the number `1` belongs at index `0`, `2` belongs at index `1`, and so on.

The **Cyclic Sort** pattern allows us to sort the array in-place with linear time complexity by matching each number to its correct target index.

### Step-by-Step Algorithm
1. **Place Numbers at Correct Indices:** Iterate through the array using a `while` loop. For the current number `nums[i]`, calculate its target index `correct_index = nums[i] - 1`.
   * If `nums[i]` is not at its correct index, and the number already sitting at `correct_index` is **not** a duplicate of `nums[i]`, swap them.
   * Do not increment the pointer `i` after a swap, as we need to evaluate the newly swapped number.
   * If the number is already in its correct spot or is a duplicate, safely increment `i`.
2. **Identify Missing Numbers:** Run a secondary loop to scan the array. If any index `i` does not hold the value `i + 1`, it means `i + 1` is missing from the array (and a duplicate number took its place). Collect these missing values into the result array.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(n)$  
  Although there is a nested evaluation logic inside the `while` loop, every element is swapped into its correct position at most once. The total number of swaps across the entire runtime is bounded by $n$, leading to a linear overall time complexity. The final identification loop also takes a single pass of $O(n)$.
* **Space Complexity:** $O(1)$  
  The sorting is performed entirely in-place by mutating the input array `nums`. No additional memory data structures are allocated. The output list does not count toward extra space complexity as per standard problem constraints.
