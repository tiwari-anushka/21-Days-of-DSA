# Day 13: Middle of the Linked List

**Problem Link:** [LeetCode #876 - Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

---

## 🚀 Approach 1: Two-Pass (Count and Traverse)

### Algorithmic Steps
1. **Count Nodes:** Initialize a counter at `0` and a pointer at the `head` of the list. Traverse the entire linked list node-by-node, incrementing the counter at each step until reaching the end (`None`).
2. **Find Middle Index:** Calculate the target middle index using integer floor division: `middle_index = total_count // 2`. This mathematical choice perfectly targets the exact middle for odd lengths, and the second middle node for even lengths.
3. **Traverse to Target:** Reset a pointer back to the `head` of the list. Run a loop that steps forward exactly `middle_index` times, then stop and return that node.

### Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N)$ 
  * The algorithm makes two sequential linear scans over the list. The first scan takes $N$ steps to count, and the second scan takes $\frac{N}{2}$ steps to reach the middle. This results in roughly $1.5N$ total operations, which simplifies asymptotically to $\mathcal{O}(N)$.
* **Space Complexity:** $\mathcal{O}(1)$
  * The solution only requires a few primitive integer variables (`count`, `middle_index`) and traversal pointers, utilizing a constant amount of auxiliary memory.

---

## ⚡ Approach 2: One-Pass (Fast & Slow Pointers)

### Algorithmic Steps
This approach utilizes **Floyd's Tortoise and Hare** cycle-finding variation to locate the midpoint in a single sweep.

1. **Setup Pointers:** Place two pointers, `slow` and `fast`, at the starting `head` node of the linked list.
2. **Simultaneous Race:** Traverse the list using a loop. In each iteration:
   * Move the `slow` pointer forward by **1 node** (`slow = slow.next`).
   * Move the `fast` pointer forward by **2 nodes** (`fast = fast.next.next`).
3. **Termination:** The loop continues as long as both `fast` and `fast.next` are valid (not `None`). 
   * For **odd-length** lists, `fast` will stop exactly on the last node.
   * For **even-length** lists, `fast` will step completely past the last node into `None`.
4. **Conclusion:** Because the `fast` pointer moves exactly twice as fast as the `slow` pointer, the moment `fast` hits the boundary or end of the list, `slow` will be resting precisely on the required middle node.

### Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N)$
  * The list is traversed in a single pass. The `fast` pointer reaches the end of the list in exactly $\frac{N}{2}$ loop iterations. Since it takes constant operations per step, the time scales linearly with the size of the list.
* **Space Complexity:** $\mathcal{O}(1)$
  * No extra data structures are created. Memory allocation is restricted solely to the two reference pointers (`slow` and `fast`), satisfying constant space requirements.
