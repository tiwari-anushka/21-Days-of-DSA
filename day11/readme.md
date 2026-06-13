# Day 11: LeetCode 142 - Linked List Cycle II

An elegant, optimal Python 3 solution to find the starting node of a cycle in a singly-linked list using **Floyd's Tortoise and Hare Algorithm** (Cycle Detection).

🔗 **Problem Link:** [LeetCode 142 - Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

---

## 🚀 Performance
* **Runtime:** 47 ms (Beats 86.11% of Python3 submissions)
* **Memory:** 22.20 MB (Beats 95.79% of Python3 submissions)

---

## 📌 Problem Description
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (**0-indexed**). It is `-1` if there is no cycle. 

> **Note:** `pos` is not passed as a parameter.

---

## 💡 Algorithm & Intuition
The solution uses a two-pointer approach known as **Floyd's Cycle-Finding Algorithm**:

1. **Phase 1 (Detecting the Cycle):** Initialize two pointers, `slow` and `fast`, at the `head`. Move `slow` by 1 step and `fast` by 2 steps. If they meet, a cycle exists. If `fast` reaches the end (`None`), there is no cycle.

2. **Phase 2 (Finding the Start of the Cycle):** Once a collision is found, reset a new pointer `current` to the `head` of the linked list. Keep `slow` at the meeting point. Move both `current` and `slow` forward exactly 1 step at a time. The node where they intersect is the starting node of the cycle.

### Mathematical Proof
Let:
* $L_1$ = Distance from the head to the start of the cycle.
* $L_2$ = Distance from the start of the cycle to the meeting point.
* $C$ = Length of the cycle.

When the pointers meet:
* Distance traveled by `slow` = $L_1 + L_2$
* Distance traveled by `fast` = $L_1 + L_2 + n \cdot C$ (where $n$ is the number of loops completed by fast)

Since `fast` travels twice as fast as `slow`:
$$2(L_1 + L_2) = L_1 + L_2 + n \cdot C$$
$$L_1 + L_2 = n \cdot C$$
$$L_1 = n \cdot C - L_2$$

This proves that the distance from the head to the cycle start ($L_1$) is exactly equal to the distance from the meeting point to the cycle start (moving forward around the cycle).

---

## ⏱️ Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N)$ 
  * Phase 1 takes at most $N$ steps to find a match where $N$ is the number of nodes. 
  * Phase 2 takes at most $N$ steps to find the cycle entrance. 
  * Overall time complexity stays linear.

* **Space Complexity:** $\mathcal{O}(1)$
  * The algorithm only creates a few pointer variables (`slow`, `fast`, `current`), utilizing constant extra space.
