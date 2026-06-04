# Day 5

## 🔗 Problem Link
[LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/).

---

## 📝 Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates [in-place](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) such that each unique element appears **at most twice**. The **relative order** of the elements must be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead place the result in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

**Constraints:**
* Do **not** allocate extra space for another array. You must do this by **modifying the input array in-place** with $O(1)$ extra memory.
* `1 <= nums.length <= 3 * 10^4`
* `nums` is sorted in non-decreasing order.

---

## 💡 Intuition & Approach: Two-Pointer Technique

A naive approach would involve deleting duplicates using methods like `del` or `.pop()`. However, deleting an element from the middle of an array forces Python to shift all subsequent elements to the left, resulting in an inefficient **$O(n^2)$** time complexity.

To solve this in **$O(n)$ time** and **$O(1)$ space**, we use a **Two-Pointer Approach** (`read` and `write`) to overwrite unwanted duplicates dynamically:

1. **Initialization:** Because the problem statement allows each element to appear up to **twice**, the first two elements (`nums[0]` and `nums[1]`) are *always valid*. We can safely start both pointers at index `2`.
2. **The Read Pointer (`read`):** Scans through the array from left to right, evaluating every element.
3. **The Write Pointer (`write`):** Tracks the index where the next valid element should be written.
4. **The Core Logic:** For every element at `nums[read]`, we compare it to the element **two positions behind the write pointer** (`nums[write - 2]`). 
   * If `nums[read] != nums[write - 2]`, it means we haven't reached three duplicates of this value yet. We copy `nums[read]` to `nums[write]` and increment `write`.
   * If they are equal, it's an invalid duplicate. We ignore it and move `read` forward.

---

## ⏳ Complexity Analysis

* **Time Complexity:** **$O(n)$** — The array is traversed exactly once by the `read` pointer, where $n$ is the length of `nums`.
* **Space Complexity:** **$O(1)$** — No additional data structures are allocated. All array manipulations and structural updates are done entirely in-place.
