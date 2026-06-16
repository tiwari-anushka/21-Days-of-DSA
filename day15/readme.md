# Day 15: Longest Substring Without Repeating Characters

**Problem Link:** [LeetCode 3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem Description
Given a string `s`, find the length of the **longest substring** without duplicate characters.

### Examples
* **Input:** `s = "abcabcbb"`  
  **Output:** `3`  
  **Explanation:** The answer is `"abc"`, with a length of 3.
* **Input:** `s = "bbbbb"`  
  **Output:** `1`  
  **Explanation:** The answer is `"b"`, with a length of 1.
* **Input:** `s = "pwwkew"`  
  **Output:** `3`  
  **Explanation:** The answer is `"wke"`, with a length of 3. (Note that `"pwke"` is a subsequence and not a substring).

---

## Approach & Algorithm: Sliding Window
To solve this problem efficiently in $O(N)$ time, we use the **Sliding Window** technique optimized with a dynamic hash set tracking unique characters.

### Step-by-Step Breakdown
1. **Initialize Pointers & Tracking:** We define a `left` pointer at index `0` to mark the start of our current window, a `max_length` variable to record the longest valid substring seen, and a hash set (`char_set`) to keep track of all unique characters inside the current window.
2. **Expand the Window (`right` pointer):** We iterate through the string using a `right` pointer, treating it as the end of our sliding window.
3. **Handle Duplicates (Shrink the Window):** Before adding the character at `s[right]` to our set, we check if it already exists in `char_set`. If it does, we have a duplicate. We must shrink our window from the left by removing `s[left]` from the set and incrementing `left` until the duplicate character is completely squeezed out of our window.
4. **Update Metrics:** Once the window contains only unique characters, we safely add `s[right]` to `char_set` and calculate the current window's size using the formula:  
   $$\text{Current Length} = \text{right} - \text{left} + 1$$  
   We update `max_length` if this current window is larger than our previous best.

---

## Complexity Analysis

| Complexity | Notation | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N)$ | Although there is a nested `while` loop, both the `left` and `right` pointers traverse the string at most once, resulting in a linear scan. |
| **Space Complexity** | $O(\min(M, N))$ | The size of the hash set is bounded by the size of the string ($N$) and the size of the character alphabet ($M$). |
