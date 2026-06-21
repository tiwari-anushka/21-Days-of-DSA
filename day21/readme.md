# Day 21: Find All Duplicates in an Array

## Problem Link
You can find the problem description and submit your solution on [LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/).

---

## Approach: Cyclic Sort
Since the numbers in the array are bounded by the range `[1, n]`, we can use the **Cyclic Sort** pattern to place each number at its correct index in-place. The correct index for any number $x$ is $x - 1$.

### Algorithm Steps:
1. **Rearrange Elements (In-place):** Iterate through the array using a `while` loop. For the current number `nums[i]`, determine its correct index: `current_index = nums[i] - 1`.
   - If the number at `nums[i]` is not equal to the number at its correct position (`nums[current_index]`), swap them.
   - Otherwise, if it's already in the correct position or it's a duplicate of a number already in the correct position, simply move the pointer `i` forward.
2. **Identify Duplicates:** Iterate through the rearranged array. Any element that is not at its correct index (i.e., `nums[i] != i + 1`) is a duplicate. Collect these elements and return them.

---

## Complexity Analysis

- **Time Complexity:** **$O(n)$** Although there is a `while` loop nested within the iteration, each swap places at least one element into its correct final position. Since an element can be swapped at most once to its correct spot, the total number of swaps across the entire execution is bounded by $n$. The subsequent loop to find duplicates also takes a single pass of $O(n)$, resulting in an overall linear time complexity.
  
- **Space Complexity:** **$O(1)$** The sorting and checking are done entirely in-place by modifying the input array. No extra data structures are used aside from the list required to store the final output, satisfying the constant extra space constraint.
