"""
169. Majority Element
https://leetcode.com/problems/majority-element/

Difficulty: Easy
Tags: array, hash-table, divide-and-conquer, sorting, counting
"""

from collections import defaultdict

import pytest


class Sorting:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Sort nums first, then pick the element at the middle.

        Time: O(n*log(n))
        Space: O(1)
        """
        nums.sort()

        return nums[len(nums) // 2]


class HashMap:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Count each element in a hash map, then pick the max.

        Time: O(n)
        Space: O(n)
        """
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        key, _ = max(counter.items(), key=lambda item: item[1])
        return key


class VotingAlgorithm:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Keep track of only the most prevalent element and count, change only
        when count dips to 0.

        Time: O(n)
        Space: O(1)
        """
        candidate, count = nums[0], 0

        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1

        return candidate


SOLUTIONS = [Sorting, HashMap, VotingAlgorithm]


@pytest.mark.parametrize("solution", SOLUTIONS, ids=lambda s: __name__)
@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param([3, 2, 3], 3, id="example-1"),
        pytest.param([2, 2, 1, 1, 1, 2, 2], 2, id="example-2"),
        pytest.param([7], 7, id="single"),
        pytest.param([4, 4, 4, 4], 4, id="all-same"),
        pytest.param([3, 3, 3, 1, 2], 3, id="majority-at-start"),
        pytest.param([1, 2, 3, 3, 3], 3, id="majority-at-end"),
        pytest.param([1, 2, 1, 2, 1], 1, id="interleaved"),
        pytest.param([2, 1, 2, 2], 2, id="even-length-minimal"),
        pytest.param([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3], 3, id="candidate-changes"),
        pytest.param([5, 1, 5, 2, 5, 3, 5], 5, id="many-distinct-minorities"),
        pytest.param([0, 1, 0], 0, id="zero-majority"),
        pytest.param([-1, -2, -1], -1, id="negative"),
        pytest.param([10**9, -(10**9), 10**9], 10**9, id="bounds"),
        pytest.param([1, 3, 1, 1, -2], 1, id="majority-loses-lead-then-recovers"),
    ],
)
def test_solution(solution, nums, expected):
    assert solution().majorityElement(nums.copy()) == expected
