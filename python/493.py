"""
https://leetcode-cn.com/problems/reverse-pairs/

493. 翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。
"""

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    res += 1
        return res


def merge_sort(nums, left, right):
    if (left >= right):
        return 0
    retval = 0
    mid = (left + right) // 2
    retval += merge_sort(nums, left, mid)
    retval += merge_sort(nums, mid+1, right)

    buf = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    # 这里是最重要的合并结果的地方
    while i <= mid:
        while j <= right and nums[i] > nums[j] * 2:
            j += 1
        # 对于左侧的每一个元素i都需要计算一次
        # 这里 j - mid - 1 表示 j 离开 mid 的间距 中间的元素的数量
        retval += j - mid - 1
        i += 1

    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            buf[k] = nums[i]
            i += 1
        else:
            buf[k] = nums[j]
            j += 1
        k += 1
    while i <= mid:
        buf[k] = nums[i]
        i += 1
        k += 1
    while j <= mid:
        buf[k] = nums[j]
        j += 1
        k += 1
    while k > 0:
        nums[left + k - 1] = buf[k-1]
        k -= 1
    return retval


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return merge_sort(nums, 0, len(nums) - 1)

