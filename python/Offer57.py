"""
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/

剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]


限制：

1 <= target <= 10^5
"""


from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        nums = list(range(1, target))
        res = []
        j, s = 0, 0
        for i, e in enumerate(nums):
            s += e
            while s >= target:
                if s == target:
                    res.append(nums[j:i+1][:])
                s -= nums[j]
                j += 1
        return res


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            val = nums[l] + nums[r]
            if val < target:
                l += 1
            elif val > target:
                r -= 1
            else:
                break
        return [nums[l], nums[r]]


