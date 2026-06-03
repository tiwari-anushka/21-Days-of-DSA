# Day 4

## 📝 Problem Description

**Problem Link:** [LeetCode 1089: Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right. 

**Note** that elements beyond the length of the original array are not written. The modifications to the input array must be done **in-place** and the function should not return anything.

### Example
- **Input:** `arr = [1, 0, 2, 3, 0, 4, 5, 0]`
- **Output:** `[1, 0, 0, 2, 3, 0, 0, 4]`

---

## 💡 Approach: Simulation with Array Modification

The challenge of this problem is modifying the array **in-place** without changing its overall fixed length or accidentally overwriting numbers we still need to process. 

### Implementation Details
Instead of creating a new array, this solution uses a standard simulation approach with a `while` loop to safely modify the array from left to right:

1. **Iteration:** We traverse the array using a pointer `i`.
2. **Zero Detection & Insertion:** When a `0` is encountered, we insert a new `0` immediately after it at position `i + 1` using the built-in `list.insert()` method. This shifts all subsequent elements to the right.
3. **Maintaining Fixed Length:** Because inserting an element increases the size of the array, we immediately use `list.pop()` to discard the extra element at the very end, keeping the array length constant.
4. **Pointer Adjustment:** We increment our pointer `i` by `2` when a zero is duplicated (skipping the newly inserted zero) to prevent an infinite loop, and by `1` normally.

---

## 📊 Complexity Analysis

- **Time Complexity:** $O(N^2)$, where $N$ is the length of the array. This is because each `list.insert()` operation shifts the remaining elements, taking $O(N)$ time in the worst-case scenario.
- **Space Complexity:** $O(1)$ auxiliary space, as all operations are performed directly on the input array without allocating extra data structures.
