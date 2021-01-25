"""
面试题 17.21. 直方图的水量
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        total = len(height)
        if total < 3:
            return 0
        left, right = 0, total - 1
        leftmax, rightmax = height[left], height[right]
        while left < right:
            if leftmax < rightmax:
                res += abs(leftmax - height[left])
                left += 1
                leftmax = max(leftmax, height[left])
            else:
                res += abs(rightmax - height[right])
                right -= 1
                rightmax = max(rightmax, height[right])
        return res

