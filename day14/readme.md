# Day 14: Fruit Into Baskets

## Problem Link
You can find the problem description and submit your solution on LeetCode: [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

---

## Approach: Sliding Window
The problem asks us to find the length of the longest contiguous subarray that contains at most **two distinct integers**. This is a classic **Sliding Window** (or Two-Pointer) problem.

### Algorithm Steps
1. **Initialize a Window:** Use two pointers, `left` and `right`, initialized to `0` to represent the boundaries of the current window of trees.
2. **Track Fruit Frequencies:** Use a hash map (or `defaultdict` in Python) to keep track of the fruit types currently inside the window and their respective counts.
3. **Expand the Window:** Iterate through the array by moving the `right` pointer forward. Add the current fruit to the hash map.
4. **Shrink the Window (If Invalid):** If the number of unique fruits in the hash map exceeds 2, move the `left` pointer to the right. Decrement the frequency of the fruits being left behind. If a fruit's frequency drops to `0`, remove it from the map entirely. Repeat this until the map size is $\le 2$.
5. **Update Max Fruits:** At each step where the window is valid, calculate the current window length (`right - left + 1`) and update the maximum fruits collected so far.

---

## Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in the `fruits` array. Although there is a nested `while` loop, the `left` pointer only moves forward and visits each element at most once across the entire execution. Thus, each element is processed at most twice (once by `right`, once by `left`).
- **Space Complexity:** $O(1)$ auxiliary space. The `basket` hash map will store at most 3 distinct fruit types before the `while` loop triggers and reduces it back to 2. Because the size of the map is strictly bounded by a constant, it utilizes constant space.
