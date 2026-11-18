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
        # From the problem
        pytest.param(
            [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6], id="example-1"
        ),
        pytest.param([1], 1, [], 0, [1], id="example-2"),
        pytest.param([0], 0, [1], 1, [1], id="example-3"),
        # One side empty
        pytest.param([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3], id="m-zero"),
        pytest.param([0], 0, [-1], 1, [-1], id="m-zero-negative"),
        pytest.param([1, 2, 3], 3, [], 0, [1, 2, 3], id="n-zero"),
        pytest.param([0], 1, [], 0, [0], id="n-zero-real-zero"),
        # Relative order of the two arrays
        pytest.param(
            [4, 5, 6, 0, 0, 0],
            3,
            [1, 2, 3],
            3,
            [1, 2, 3, 4, 5, 6],
            id="nums2-all-smaller",
        ),
        pytest.param(
            [1, 2, 3, 0, 0, 0],
            3,
            [4, 5, 6],
            3,
            [1, 2, 3, 4, 5, 6],
            id="nums2-all-larger",
        ),
        pytest.param(
            [1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6], id="interleaved"
        ),
        pytest.param([1, 0], 1, [-3], 1, [-3, 1], id="single-nums2-goes-first"),
        pytest.param([2, 0], 1, [0], 1, [0, 2], id="single-nums2-zero-goes-first"),
        pytest.param([-2, 4, 0], 2, [0], 1, [-2, 0, 4], id="nums1-holds-largest"),
        # Uneven lengths
        pytest.param([1, 0, 0, 0], 1, [0, 2, 3], 3, [0, 1, 2, 3], id="nums2-longer"),
        pytest.param([1, 2, 3, 4, 0], 4, [0], 1, [0, 1, 2, 3, 4], id="nums1-longer"),
        # Equal values
        pytest.param(
            [1, 2, 2, 0, 0], 3, [2, 2], 2, [1, 2, 2, 2, 2], id="ties-across-arrays"
        ),
        pytest.param([2, 2, 0, 0], 2, [2, 2], 2, [2, 2, 2, 2], id="all-equal"),
        # Values vs the 0 placeholders
        pytest.param(
            [-5, -3, 0, 0], 2, [-4, -1], 2, [-5, -4, -3, -1], id="all-negative"
        ),
        pytest.param([-2, 0], 1, [-3], 1, [-3, -2], id="negative-nums2-goes-first"),
        pytest.param(
            [-1, 0, 0], 2, [-2], 1, [-2, -1, 0], id="real-zero-before-placeholder"
        ),
        pytest.param(
            [-(10**9), 10**9, 0], 2, [0], 1, [-(10**9), 0, 10**9], id="value-bounds"
        ),
    ],
)
def test_solution(solution, nums1, m, nums2, n, expected):
    nums1 = nums1.copy()
    assert solution().merge(nums1, m, nums2, n) is None
    assert nums1 == expected
