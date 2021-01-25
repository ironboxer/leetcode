"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[left] == target or nums[right] == target or nums[mid] == target:
                return True
            # nums[left: mid] 有序
            # 这个地方不可以用 <=
            if nums[left] < nums[mid]:
                # target in nums[left: mid]
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                # target not in nums[left: mid]
                else:
                    left = mid + 1
            # nums[mid: right] 有序
            # 这个地方不可以用 >=
            elif nums[right] > nums[mid]:
                # target in nums[mid: right]
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                # target not in nums[mid: right]
                else:
                    right = mid - 1
            else:
                left, right = left + 1, right - 1
        return False

# 你有完全搞清楚这个算法吗?


if __name__ == '__main__':
    nums = [1, 3, 1, 1, 1]
    target = 3
    print(Solution().search(nums, target))

    nums = [1, 2, 1]
    target = 0
    print(Solution().search(nums, target))

    nums = [3, 1]
    target = 0
    print(Solution().search(nums, target))

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))

    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    print(Solution().search(nums, target))
