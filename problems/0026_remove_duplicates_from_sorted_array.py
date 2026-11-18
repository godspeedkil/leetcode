"""
26. Remove Duplicates From Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Difficulty: Easy
Tags: array, two-pointers
"""

import pytest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Keep pair of pointers, one for insertion, the other for exploration.

        Time: O(n)
        Space: O(1)
        """
        k = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[k - 1]:
                nums[k] = nums[j]
                k += 1

        return k


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([1, 1, 2], [1, 2], id="example-1"),
        pytest.param([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], id="example-2"),
        pytest.param([1], [1], id="single"),
        pytest.param([1, 1], [1], id="pair-equal"),
        pytest.param([1, 2], [1, 2], id="pair-distinct"),
        pytest.param([5, 5, 5, 5], [5], id="all-same"),
        pytest.param([-3, -1, 0, 2, 7], [-3, -1, 0, 2, 7], id="all-unique"),
        pytest.param([1, 1, 1, 2, 3], [1, 2, 3], id="dupes-at-start"),
        pytest.param([1, 2, 3, 3, 3], [1, 2, 3], id="dupes-at-end"),
        pytest.param([1, 2, 2, 2, 3], [1, 2, 3], id="dupes-in-middle"),
        pytest.param([1, 1, 2, 2, 3, 3], [1, 2, 3], id="every-value-doubled"),
        pytest.param([-100, -100, -50, 0, 0, 100], [-100, -50, 0, 100], id="bounds"),
    ],
)
def test_solution(nums, expected):
    nums = nums.copy()
    k = Solution().removeDuplicates(nums)
    assert k == len(expected)
    assert nums[:k] == expected
