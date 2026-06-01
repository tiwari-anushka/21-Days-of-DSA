# Day 2: Remove Linked List Elements 🚀

Welcome to Day 2 of the **#DrGVishwanathan 21 Days of DSA Challenge**! Today, I tackled a classic linked list manipulation problem on LeetCode.

## 📝 Problem Description
Given the `head` of a singly-linked list and an integer `val`, remove all the nodes of the linked list that have `Node.val == val`, and return the new head.

**Example:**
* **Input:** `head = [1,2,6,3,4,5,6]`, `val = 6`
* **Output:** `[1,2,3,4,5]`

---

## 💡 Conceptual Approach: The Dummy Node Technique

When deleting nodes from a singly-linked list, the trickiest edge case occurs when the node(s) to delete are at the very beginning (the `head`). 

To handle this cleanly without writing bulky conditional logic, I utilized a **Dummy Node**:
1. **Setup:** Created a dummy node (`prev = ListNode(0)`) and pointed its `.next` directly to the `head`.
2. **Traversal:** Used a pointer (`curr`) starting at the dummy node to look ahead at `curr.next`.
3. **Deletion:** * If the next node's value matches the target `val`, we skip over it by reassigning pointers: `curr.next = curr.next.next`.
   * If it doesn't match, we safely step forward: `curr = curr.next`.
4. **Result:** Returning `prev.next` gives us the modified list, even if the original head node was deleted.

---

## 📊 Complexity Analysis

### ⏱️ Time Complexity: $O(N)$
* **Explanation:** We iterate through the entire linked list exactly once, where $N$ is the total number of nodes in the list. 
* **Details:** Each node's value is checked a single time. Reassigning pointers (`curr.next = curr.next.next`) happens in $O(1)$ constant time, ensuring an optimal linear runtime performance.

### 💾 Space Complexity: $O(1)$
* **Explanation:** The algorithm operates entirely **in-place**.
* **Details:** We only allocate a fixed amount of extra memory for the single dummy node and the traversal pointer (`curr`). Because we are reassigning pointers of the existing list rather than creating a new list, the memory footprint remains constant regardless of how large the input linked list grows.

---
