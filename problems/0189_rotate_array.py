"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Difficulty: Medium
Tags: array, math, two-pointers
"""

from math import gcd

import pytest


class IndividualRotations:
    """
    Approach: Mutate the input array k times, rotating one space each.

    Time: O(k*n)
    Space: O(1)
    """

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for _ in range(k):
            last = nums[n - 1]
            for i in range(n - 2, -1, -1):
                nums[i + 1] = nums[i]
            nums[0] = last


class ExtraArray:
    """
    Approach: Assign a new array and populate each element in its correct
    new position.

    Time: O(n)
    Space: O(n)
    """

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        a = [0] * n

        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a


class OptimizedRotations:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Approach: Cyclic replacements. Move each element to its final position
        per cycle, until looped. gcd(n, k) gives you how many cycles there are.

        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        # Avoid unnecessary rotations
        k %= n
        if k == 0:
            return

        for start in range(gcd(n, k)):
            carried = nums[start]
            i = start
            while True:
                i = (i + k) % n
                nums[i], carried = carried, nums[i]
                if i == start:
                    break


class Reversing:
    """
    Approach: Reversing the array, then reversing both subarrays split by k
    actually gives the correct result.

    Time: O(n)
    Space: O(1)
    """

    def _reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        self._reverse(nums, 0, n - 1)
        self._reverse(nums, 0, k - 1)
        self._reverse(nums, k, n - 1)


INT_MIN, INT_MAX = -(2**31), 2**31 - 1
SOLUTIONS = [IndividualRotations, ExtraArray, OptimizedRotations, Reversing]


@pytest.mark.parametrize("solution", SOLUTIONS, ids=lambda s: s.__name__)
@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        # From the problem
        pytest.param([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4], id="example-1"),
        pytest.param([-1, -100, 3, 99], 2, [3, 99, -1, -100], id="example-2"),
        # Size boundaries
        pytest.param([5], 0, [5], id="single-k-zero"),
        pytest.param([1, 2], 1, [2, 1], id="two-elements"),
        pytest.param([1, 2], 3, [2, 1], id="two-elements-k-wraps-odd"),
        # k relative to n
        pytest.param([1, 2, 3], 0, [1, 2, 3], id="k-zero"),
        pytest.param([1, 2, 3, 4], 1, [4, 1, 2, 3], id="k-one"),
        pytest.param([1, 2, 3, 4], 3, [2, 3, 4, 1], id="k-n-minus-one"),
        pytest.param([1, 2, 3], 3, [1, 2, 3], id="k-equals-n"),
        pytest.param([1, 2, 3], 4, [3, 1, 2], id="k-n-plus-one"),
        pytest.param([1, 2, 3], 6, [1, 2, 3], id="k-multiple-of-n"),
        # gcd(n, k) > 1: cyclic replacement needs more than one cycle
        pytest.param([1, 2, 3, 4], 2, [3, 4, 1, 2], id="k-half-n"),
        pytest.param([1, 2, 3, 4, 5, 6], 2, [5, 6, 1, 2, 3, 4], id="gcd-2"),
        pytest.param([1, 2, 3, 4, 5, 6], 3, [4, 5, 6, 1, 2, 3], id="gcd-3"),
        # Duplicates: catch solutions that track position by value
        pytest.param([7, 7, 7, 7], 2, [7, 7, 7, 7], id="all-same"),
        pytest.param([2, 2, 1], 1, [1, 2, 2], id="duplicates-direction"),
        pytest.param([-2, 2, -2], 1, [-2, -2, 2], id="duplicates-in-cycle"),
        pytest.param([0, 0, -1, 1], 2, [-1, 1, 0, 0], id="duplicates-gcd-2"),
        # Values
        pytest.param([INT_MIN, 0, INT_MAX], 1, [INT_MAX, INT_MIN, 0], id="int-bounds"),
    ],
)
def test_solution(solution, nums, k, expected):
    nums = nums.copy()
    assert solution().rotate(nums, k) is None
    assert nums == expected
