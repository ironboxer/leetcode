"""
https://leetcode.com/problems/trapping-rain-water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        retval = 0
        max_left_h, max_right_h = 0, 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                if height[left] > max_left_h:
                    max_left_h = height[left]
                else:
                    retval += max_left_h - height[left]
                    left += 1
            else:
                if height[right] > max_right_h:
                    max_right_h = height[right]
                else:
                    retval += max_right_h - height[right]
                    right -= 1

        return retval


# 总是有人会想出很巧妙的方法, 累计的都是高度的变化信息, 没有水平位移信息了

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
