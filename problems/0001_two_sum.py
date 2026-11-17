"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Tags: array, hash-table
"""

import pytest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # One pass: remember each value's index, look up the complement.
        seen: dict[int, int] = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ],
)
def test_solution(args, expected):
    assert Solution().twoSum(*args) == expected
