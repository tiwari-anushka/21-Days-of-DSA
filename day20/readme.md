# Day 20: Find the Duplicate Number

## 🔗 Problem Link
You can find the problem description and test cases on [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/).

## 📝 Problem Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. There is only **one repeated number** in `nums`, return this repeated number.

### Example
* **Input:** `nums = [1, 3, 4, 2, 2]`
* **Output:** `2`

---

## 💡 Approach: Cyclic Sort

Since the numbers in the array are tightly bounded in the range `[1, n]` and the array has a size of `n + 1`, we can map each number to its ideal index. In a perfectly sorted array without duplicates, the number `val` should sit at index `val - 1`. 

### Algorithm Steps:
1. **Sort Cycles:** Iterate through the array using a `while` loop. For the current number `nums[i]`, calculate its intended target position: `correct_index = nums[i] - 1`.
2. **Swap Misplaced Elements:** If the number at the current index doesn't match the number at its target index (`nums[i] != nums[correct_index]`), swap them. This places the current number in its correct home.
3. **Advance Pointer:** If they already match (meaning either the number is already home or its duplicate is already sitting there), simply move the pointer `i` forward.
4. **Identify the Duplicate:** Run a final linear scan through the array. The first index `i` where `nums[i] != i + 1` reveals the duplicate value.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(n)$
  * Although there is a `while` loop containing swaps, each element is swapped into its correct position at most once. The pointer `i` increments $n$ times. Thus, the total operations are bounded by $O(n)$.
* **Space Complexity:** $O(1)$
  * The algorithm sorts the elements in place, requiring no extra memory allocations.

---

## ⚠️ Interviewer Note
While the **Cyclic Sort** pattern is highly efficient with $O(n)$ time and $O(1)$ space, it **modifies the input array**. 

If an interviewer strictly enforces the constraint *"You must solve the problem without modifying the array nums"*, the optimal approach would shift to **Floyd's Tortoise and Hare (Cycle Detection)** algorithm.
