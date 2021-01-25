"""
https://leetcode-cn.com/problems/sort-an-array/

912. 排序数组
给你一个整数数组 nums，请你将该数组升序排列。



示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]


提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
"""

from typing import List


def partation(nums, left, right):
    pivot = nums[left]
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return left


def quick_sort(nums, left, right):
    pivot = partation(nums, left, right)
    if left < pivot - 1:
        quick_sort(nums, left, pivot - 1)
    if pivot < right:
        quick_sort(nums, pivot, right)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':

    import random
    nums = random.sample(range(10), 10)
    print(nums)
    print(Solution().sortArray(nums))

