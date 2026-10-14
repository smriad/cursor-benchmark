"""Binary search on a sorted list — contains a subtle bug for benchmark prompts."""

from __future__ import annotations


def binary_search(sorted_values: list[int], target: int) -> int:
    """Return index of target, or -1 if missing."""
    left, right = 0, len(sorted_values) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_values[mid] == target:
            return mid
        if sorted_values[mid] < target:
            left = mid  # bug: should advance past mid
        else:
            right = mid - 1
    return -1
