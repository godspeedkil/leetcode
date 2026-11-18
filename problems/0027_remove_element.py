"""
27. Remove Element
https://leetcode.com/problems/remove-element/

Difficulty: Easy
Tags: array, two-pointers
"""

import pytest


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Keep a single pointer, update as you go along.

        Time: O(n)
        Space: O(1)
        """
        i = 0

        for num in nums:
            if num != val:
                nums[i] = num
                i += 1

        return i


@pytest.mark.parametrize(
    ("nums", "val", "expected"),
    [
        pytest.param([3, 2, 2, 3], 3, [2, 2], id="example-1"),
        pytest.param([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4], id="example-2"),
        pytest.param([], 0, [], id="empty"),
        pytest.param([1], 1, [], id="single-match"),
        pytest.param([1], 2, [1], id="single-no-match"),
        pytest.param([3, 3, 3, 3], 3, [], id="all-match"),
        pytest.param([1, 2, 3, 4], 5, [1, 2, 3, 4], id="none-match"),
        pytest.param([2, 2, 1, 3], 2, [1, 3], id="matches-at-start"),
        pytest.param([1, 3, 2, 2], 2, [1, 3], id="matches-at-end"),
        pytest.param([1, 2, 1, 2, 1], 1, [2, 2], id="alternating"),
        pytest.param([4, 1, 4, 4, 2, 4], 4, [1, 2], id="match-is-last-swapped-in"),
        pytest.param([0, 0, 1, 0], 0, [1], id="val-zero"),
        pytest.param([0, 50, 25], 100, [0, 50, 25], id="val-outside-num-range"),
    ],
)
def test_solution(nums, val, expected):
    nums = nums.copy()
    k = Solution().removeElement(nums, val)
    assert k == len(expected)
    assert sorted(nums[:k]) == sorted(expected)
