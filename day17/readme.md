# Day 17: Max Consecutive Ones III

An elegant, optimized approach to solving the [LeetCode 1004 - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) problem using the Sliding Window technique.

---

## 📝 Problem Statement

Given a binary array `nums` and an integer `k`, return the *maximum number of consecutive `1`s* in the array if you can flip at most `k` `0`s.

### Example 1
> **Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2`  
> **Output:** `6`  
> **Explanation:** `[1,1,1,0,0,1,1,1,1,1,1]` (underlined numbers were flipped from 0 to 1). The longest subarray is underlined.

### Example 2
> **Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]`, `k = 3`  
> **Output:** `10`  
> **Explanation:** `[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]` (underlined numbers were flipped from 0 to 1). The longest subarray is underlined.

---

## 💡 Algorithmic Approach: Sliding Window

The problem asks for the longest contiguous subarray containing mostly `1`s, with a restriction that it can contain at most `k` zeros (since we can flip at most `k` zeros into ones). 

Instead of generating all possible subarrays, we use a **dynamic sliding window** defined by two pointers, `left` and `right`.

### How it Works:
1. **Expand the Window:** We iterate through the array using the `right` pointer. If `nums[right]` is `0`, we increment our `zero_count`.
2. **Shrink the Window:** If `zero_count` exceeds `k`, it means the current window is invalid (we used more than `k` flips). We shrink the window from the left by moving the `left` pointer forward. If the element leaving the window (`nums[left]`) was a `0`, we decrement `zero_count`.
3. **Update Maximum Length:** At each step, if the window is valid, we calculate its length (`right - left + 1`) and update our `max_length`.

---

## 📊 Complexity Analysis

* **Time Complexity:** $O(N)$, where $N$ is the length of the `nums` array. Although there is a nested `while` loop, the `left` pointer only moves forward and visits each element at most once across the entire runtime. Thus, each element is processed a maximum of two times (once by `right`, once by `left`), ensuring a linear runtime complexity.
* **Space Complexity:** $O(1)$ auxiliary space, as we only use a few tracking variables (`left`, `zero_count`, `max_length`) that take up constant memory regardless of the input size.
