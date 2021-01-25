"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def f(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        res = [-1, -1]
        left, right = 0, len(nums) - 1
        while True:
            p = f(nums, left, right, target)
            if p == -1:
                break
            res[0] = p
            right = p - 1

        left, right = 0, len(nums) - 1
        while True:
            p = f(nums, left, right, target)
            if p == -1:
                break
            res[-1] = p
            left = p + 1

        return res


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def f(nums, left, right, target):
            hit = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    hit = mid
                    right = mid - 1

            return hit
        
        def g(nums, left, right, target):
            hit = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    hit = mid
                    left = mid + 1

            return hit
        
        left, right = 0, len(nums) - 1
        res = [f(nums, left, right, target), g(nums, left, right, target)]
        return res


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution2().searchRange(nums, target))
