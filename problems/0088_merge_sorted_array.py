"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Difficulty: Easy
Tags: array, two-pointers, sorting
"""

import pytest


class MergeAndSort:
    """
    Merge nums2 into nums1 first, then sort.

    Time: O((m + n)*log(m + n))
    Space: O(1), not counting pre-allocated space
    """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of nums2 into the end of nums1
        for i in range(n):
            nums1[i + m] = nums2[i]

        # Sort nums1 list in-place
        nums1.sort()


class TwoPointers:
    """
    Keep two pointers for the arrays, sort as you go from right to left.

    Time: O(m + n)
    Space: O(1)
    """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if not m or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


SOLUTIONS = [MergeAndSort, TwoPointers]


@pytest.mark.parametrize("solution", SOLUTIONS, ids=lambda s: s.__name__)
@pytest.mark.parametrize(
    ("nums1", "m", "nums2", "n", "expected"),
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([-2, 4, 0], 2, [0], 1, [-2, 0, 4]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
    ],
)
def test_solution(solution, nums1, m, nums2, n, expected):
    nums1 = nums1.copy()
    assert solution().merge(nums1, m, nums2, n) is None
    assert nums1 == expected
