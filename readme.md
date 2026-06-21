# Day 18: Missing Number

## Problem Description
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

- **Problem Link:** [LeetCode - Missing Number](https://leetcode.com/problems/missing-number/)
- **Time Complexity Goal:** $O(n)$
- **Space Complexity Goal:** $O(1)$

---

## Approach: Cyclic Sort

The most intuitive approach might involve sorting the array ($O(n \log n)$) or using a hash set ($O(n)$ extra space). However, to achieve both **linear time** and **constant space**, we can leverage the **Cyclic Sort** pattern.

### Intuition
Since the array contains `n` distinct numbers ranging from `0` to `n`, every number ideally belongs at the index equal to its value (e.g., `0` belongs at index `0`, `1` belongs at index `1`, and so on). 

We can iterate through the array and try to place each number at its "correct index" by swapping. The only exception is the number `n`, which cannot be placed because the maximum index of the array is `n - 1`.

### Algorithm Steps
1. **Sort Phase:** Iterate through the array using a pointer `i`. If the current number `nums[i]` is less than `n` and is not at its correct position (`nums[i] != nums[nums[i]]`), swap it with the element at its correct index. Otherwise, move the pointer `i` forward.
2. **Find Phase:** Scan the array a second time. The first index `i` where `nums[i] != i` is the missing number.
3. **Edge Case:** If all numbers from `0` to `n-1` are in their correct positions, then `n` is the missing number.

---

## Complexity Analysis

- **Time Complexity:** $O(n)$  
  Although there is a nested loop mechanism structurally, each element is swapped into its correct position at most once. The pointer `i` is incremented only when an element is already in the right place or is equal to `n`. Because an element can be swapped at most once to its correct spot, the algorithm makes at most $2n$ total operations, resulting in a strict linear time complexity.
  
- **Space Complexity:** $O(1)$  
  The cyclic sorting is performed entirely in-place by rearranging the elements within the input array. No additional data structures (like HashMaps or extra arrays) are allocated, satisfying the constant space requirement.
