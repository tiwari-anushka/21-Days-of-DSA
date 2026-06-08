# 📅 Day 9: Dutch National Flag Sorting Algorithm

An efficient implementation of the classic **Dutch National Flag (DNF)** sorting problem, originally proposed by Edsger Dijkstra. This project breaks down the approach as outlined in the classic [Coderbyte Tutorial](https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem).

The goal is to sort an array containing three distinct elements (e.g., `0`s, `1`s, and `2`s) in a single pass without using any extra memory.

## 🚀 Efficiency

* **Time Complexity:** $O(n)$ – The array is scanned exactly once.
* **Space Complexity:** $O(1)$ – The sorting is done completely **in-place**, requiring no auxiliary arrays.

---

## 💡 The Approach

The problem is solved using a **Three-Pointer approach** that partitions the array into four distinct zones during execution:

1.  **Red Zone (`0`s):** Elements from index `0` to `low - 1`.
2.  **White Zone (`1`s):** Elements from index `low` to `mid - 1`.
3.  **Unsorted Zone:** Elements from index `mid` to `high`.
4.  **Blue Zone (`2`s):** Elements from index `high + 1` to the end of the array.

As the `mid` pointer scans the array, elements are swapped into their correct zones, shrinking the unsorted region until `mid` passes `high`.

---

## 🛠️ The Algorithm

1.  Initialize three pointers:
    * `low = 0` (Tracks the boundary for `0`s)
    * `mid = 0` (Scans the array)
    * `high = len(arr) - 1` (Tracks the boundary for `2`s)
2.  Loop while `mid <= high`:
    * **Case `0`:** If the element at `mid` is `0`, swap it with the element at `low`. Increment both `low` and `mid` by 1.
    * **Case `1`:** If the element at `mid` is `1`, it is already in the correct middle region. Just increment `mid` by 1.
    * **Case `2`:** If the element at `mid` is `2`, swap it with the element at `high`. Decrement `high` by 1. *(Note: Do not increment `mid` here, as the new element swapped from `high` must be evaluated in the next iteration).*

---
