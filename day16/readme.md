# Day 16: Longest Repeating Character Replacement

## Problem Link
[LeetCode #424 - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## Approach: Sliding Window (Two Pointers)

Instead of checking every single substring (which would be too slow), we use a **sliding window** approach with a `left` and `right` pointer to find the maximum valid window dynamically.

### Intuition
For any given substring window from index `left` to `right`:
1. The **total length** of the window is `(right - left + 1)`.
2. To make all characters in this window identical, the most efficient strategy is to keep the **most frequent character** as it is, and change all the *other* characters to match it.
3. The number of characters we need to replace is calculated as:
   $$\text{Replacements Needed} = \text{Window Length} - \text{Max Frequency}$$

As long as the $\text{Replacements Needed} \le k$, the current window is considered **valid**. If it exceeds $k$, the window is invalid, and we must shrink it from the left.

---

## Algorithm Steps

1. **Initialize State:** * A hash map/dictionary `count` to store the frequency of characters in the current window.
   * `left` pointer at `0`.
   * `max_freq` to keep track of the highest frequency of any single character seen in the current window.
   * `max_length` to store the maximum valid window size found.

2. **Expand the Window:** Move the `right` pointer from `0` to the end of the string.
   * Add the character at `s[right]` to the frequency map.
   * Update `max_freq` if the current character's frequency is higher than the previous maximum.

3. **Shrink the Window (If Invalid):** * Check if the current window requires more than `k` replacements.
   * If `(right - left + 1) - max_freq > k`, the window is invalid. Decrement the count of `s[left]` in the map and increment the `left` pointer by `1`.

4. **Update Max Length:** At each step, record the maximum size of a valid window (`right - left + 1`).

---

## Complexity Analysis

| Complexity | Time | Space |
| :--- | :--- | :--- |
| **Analysis** | **$O(N)$** | **$O(1)$** |

* **Time Complexity:** $O(N)$, where $N$ is the length of the string `s`. Both the `right` and `left` pointers slide across the string at most once, resulting in a linear scan.
* **Space Complexity:** $O(1)$ auxiliary space. The `count` hash map will store at most 26 key-value pairs (since the input contains only uppercase English letters), which takes constant space.
