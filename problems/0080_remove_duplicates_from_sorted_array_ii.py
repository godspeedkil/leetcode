"""
80. Remove Duplicates From Sorted Array Ii
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Difficulty: Easy
Tags: array, two-pointers
"""

import pytest


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Two pointers, start count on every new element, once count > 2,
        move lagging pointer up.

        Time: O(n)
        Space: O(1)
        """
        i, count = 0, 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                count = 0
            if count < 2:
                i += 1
                nums[i] = nums[j]
                count += 1

        return i + 1


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3], id="example-1"),
        pytest.param(
            [0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3], id="example-2"
        ),
        pytest.param([1], [1], id="single"),
        pytest.param([1, 1], [1, 1], id="pair"),
        pytest.param([1, 1, 1], [1, 1], id="triple"),
        pytest.param([2, 2, 2, 2, 2, 2], [2, 2], id="all-same"),
        pytest.param([-3, 0, 4], [-3, 0, 4], id="all-unique"),
        pytest.param([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3], id="all-exactly-twice"),
        pytest.param([1, 1, 1, 1, 2, 3], [1, 1, 2, 3], id="run-at-start"),
        pytest.param([1, 2, 2, 2, 2, 3], [1, 2, 2, 3], id="run-in-middle"),
        pytest.param([1, 2, 3, 3, 3, 3], [1, 2, 3, 3], id="run-at-end"),
        pytest.param(
            [1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 2, 2, 3, 3], id="back-to-back-runs"
        ),
        pytest.param(
            [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], [1, 2, 2, 3, 3, 4, 4], id="mixed-counts"
        ),
        pytest.param([-1, -1, -1, 0, 0, 0, 1], [-1, -1, 0, 0, 1], id="crosses-zero"),
        pytest.param(
            [-10_000] * 3 + [10_000] * 3,
            [-10_000, -10_000, 10_000, 10_000],
            id="bounds",
        ),
    ],
)
def test_solution(nums, expected):
    nums = nums.copy()
    k = Solution().removeDuplicates(nums)
    assert k == len(expected)
    assert sorted(nums[:k]) == sorted(expected)
