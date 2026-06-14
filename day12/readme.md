# Day 12: LeetCode 202 - Happy Number

## Problem Link
You can find the problem description and test cases on LeetCode here: [Happy Number](https://leetcode.com/problems/happy-number/)

---

## Approach & Algorithm: Fast and Slow Pointers
Instead of tracking every seen number in a Hash Set (which consumes extra memory), this solution uses **Floyd's Cycle-Finding Algorithm** (also known as the **Tortoise and the Hare algorithm**).

### The Concept
Think of the sequences of numbers generated as a track:
* If the number is **happy**, the chain will eventually reach a dead end at `1` and stay there indefinitely ($1^2 = 1$).
* If the number is **unhappy**, it will get stuck in an endless circular loop (e.g., $4 \rightarrow 16 \rightarrow 37 \rightarrow 58 \rightarrow 89 \rightarrow 145 \rightarrow 42 \rightarrow 20 \rightarrow 4$).

By using two pointers running at different speeds, we can detect if a loop exists:
1. **`slow` pointer:** Advances by calculating the sum of squared digits **once** per step.
2. **`fast` pointer:** Advances by calculating the sum of squared digits **twice** per step.

If there is a cycle, the `fast` pointer will eventually catch up to (`lap`) the `slow` pointer. If they meet at any number other than `1`, the number is unhappy. If `fast` hits `1`, the number is happy.

---

## Complexity Analysis

### Time Complexity: $\mathcal{O}(\log n)$
* Digits extraction takes time proportional to the number of digits, which is $\mathcal{O}(\log_{10} n)$.
* For numbers larger than 3 digits, the digit squaring process reduces the value rapidly. For example, the largest possible sum for a 3-digit number $999$ is $9^2 + 9^2 + 9^2 = 243$.
* Once the value falls below 243, it either converges directly to 1 or enters a cycle of pre-defined, small constants. The loop runs in constant steps once inside this range.

### Space Complexity: $\mathcal{O}(1)$
* Unlike the traditional Hash Set approach which scales up in memory dynamically based on tracking history, this algorithm uses only a couple of fixed pointer variables (`slow` and `fast`).
* This achieves absolute **Constant Space** efficiency.

---

## Performance Results
* **Runtime:** `0 ms` (Beats 100.00% of Python3 submissions)
* **Memory:** `19.16 MB` (Beats 89.90% of Python3 submissions)
