"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""

from typing import List


def partation(nums, left, right):
    """
    large to small
    """
    pivot = nums[left]
    while left <= right:
        while left <= right and nums[left] > pivot:
            left += 1
        while left <= right and nums[right] < pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return left


def quick_sort(nums, left, right):
    if left < right:
        pivot = partation(nums, left, right)
        quick_sort(nums, left, pivot-1)
        quick_sort(nums, pivot, right)


def quick_select(nums, left, right, target):
    while left < right:
        pivot = partation(nums, left, right)
        if pivot <= target:
            left = pivot
        else:
            right = pivot - 1

    return nums[left]


class Solution0:
    """
    全排序的方式
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        quick_sort(nums, left, right)
        return nums[k-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        return quick_select(nums, left, right, k-1)


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))

