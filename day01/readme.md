# Day 1: Two Sum

## Problem Link
[LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## My Approach
1. **Brute Force:** Used a nested loop to check every pair. ($O(n^2)$ time complexity).
2. **Optimized Approach:** Used a Hash Map (Dictionary) to store the complement (`target - nums[i]`) as we iterate. This allows us to find the matching pair in a single pass.

## Complexity
- **Time Complexity:** $O(n)$ because we traverse the list containing $n$ elements only once.
- **Space Complexity:** $O(n)$ to store the elements in the hash map.
