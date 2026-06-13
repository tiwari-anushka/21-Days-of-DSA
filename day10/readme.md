# Day 10: Linked List Cycle

🔗 **Problem Link:** [LeetCode - Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

## 📝 Problem Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

---

## 🚀 Solution Approach: Floyd's Tortoise and Hare Algorithm

This solution utilizes **Floyd's Cycle-Finding Algorithm** (also known as the Two-Pointer technique), which is the most optimal way to detect a cycle in a linked list.

### How It Works:
1. Initialize two pointers, `slow` and `fast`, both pointing to the `head` of the linked list.
2. Traverse the linked list by moving the `slow` pointer by **one step** (`slow = slow.next`) and the `fast` pointer by **two steps** (`fast = fast.next.next`) at a time.
3. If there is no cycle, the `fast` pointer will eventually reach the end of the list (`None`), and we can safely return `False`.
4. If a cycle exists, the `fast` pointer will eventually loop around and catch up to the `slow` pointer. When `fast == slow`, a cycle is confirmed, and we return `True`.

### Complexity Analysis:
* **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. If no cycle exists, the fast pointer reaches the end in $N/2$ steps. If a cycle exists, the fast pointer catches up to the slow pointer in linear time relative to the cycle length.
* **Space Complexity:** $O(1)$, because we only use two pointers (`slow` and `fast`) regardless of the size of the linked list. This satisfies the optimal memory constraint.

---

## 📊 Performance Summary

* **Status:** Accepted 🎉
* **Language:** Python3
* **Runtime:** 52 ms (Beats ~68.01% of Python3 submissions)
* **Memory Usage:** 22.47 MB (Beats ~85.65% of Python3 submissions)
