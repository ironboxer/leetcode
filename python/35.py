"""
https://leetcode.com/problems/search-insert-position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        for i, e in enumerate(nums):
            if target <= e:
                return i
        return N


if __name__ == "__main__":
    cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 0, 0),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 2, 1),
    ]
    for nums, target, pos in cases:
        print(nums, target, pos)
        assert Solution().searchInsert(nums, target) == pos
