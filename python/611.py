"""
https://leetcode-cn.com/problems/valid-triangle-number/

611. 有效三角形的个数
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
"""


# simple and stupid

from typing import List

from itertools import combinations

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        for a, b, c in combinations(nums, 3):
            if a + b > c and a + c > b and b + c > a:
                res += 1
        return res


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        total = len(nums)
        nums.sort()
        for i in range(total - 2):
            if nums[i] == 0:
                continue

            k = i + 2
            for j in range(i+1, total - 1):
                while k < total and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1

        return res


