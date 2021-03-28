"""
https://leetcode.com/problems/search-in-rotated-sorted-array

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4


"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= target <= nums[mid]:
                return bsearch(nums, left, mid, target)
            elif nums[mid] <= target <= nums[right]:
                return bsearch(nums, mid, right, target)
            else:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                elif nums[mid] <= nums[right]:
                    right = mid - 1
                else:
                    return -1
        return -1



# make it simple and stupid
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif nums[l] <= target < val:
                r = mid - 1
            elif val < target <= nums[r]:
                l += 1
            else:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                l, r = l + 1, r - 1
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    for i, e in enumerate(nums):
        print(nums, e, i)
        assert Solution().search(nums, e) == i

# 一个土鳖的方法, 但是自己理解。其他的方法总是记不住.
