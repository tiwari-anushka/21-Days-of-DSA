# Day 3

**Problem Link:** [LeetCode 82 - Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem Description
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list **sorted** as well.

### Examples
* **Input:** `head = [1,2,3,3,4,4,5]`  
  **Output:** `[1,2,5]`
* **Input:** `head = [1,1,1,2,3]`  
  **Output:** `[2,3]`

---

## Approach: Sentinel (Dummy) Node + Two Pointers

Since the linked list is already sorted, all duplicate elements are guaranteed to be adjacent to one another. The challenge arises when the head of the list itself contains duplicate values, meaning the head needs to be deleted. 

To handle edge cases cleanly, this solution uses a **Sentinel (Dummy) Node** paired with a **Two-Pointer** technique.

### Algorithm Steps
1. **Sentinel Node Initialization:** Create a `dummy` node that points to the `head` of the list. Initialize a predecessor pointer (`pred`) at the `dummy` node.
2. **Scan the List:** Iterate through the list using the `head` pointer.
3. **Detect Duplicates:** If `head` and `head.next` share the same value, enter an inner loop to skip *all* nodes with this duplicate value. Move `head` forward until it rests on the last duplicate node of that sub-sequence.
4. **Link Around Duplicates:** Update `pred.next` to point to `head.next` (bypassing the entire block of duplicates). Note that `pred` itself does not move forward yet, as the new node must be evaluated for duplicates in the next iteration.
5. **Move Predecessor:** If no duplicate is detected, it is safe to shift the `pred` pointer forward (`pred = pred.next`).
6. **Advance Strategy:** Advance the `head` pointer in every iteration (`head = head.next`) to continue scanning.

---

## Complexity Analysis

* **Time Complexity:** $O(N)$  
  Although there is a nested `while` loop, each node in the linked list is traversed at most twice (once by the inner loop to skip duplicates, and once by the outer loop). Therefore, the overall time complexity remains strictly linear relative to the number of nodes $N$.
  
* **Space Complexity:** $O(1)$  
  The algorithm modifies the node connections in-place using existing pointers. No extra data structures are allocated, achieving constant auxiliary space complexity.
