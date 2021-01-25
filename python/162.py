"""
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity.


# 这里的题意非常重要

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i, e in enumerate(nums):
            if i == 0 and 1 < n and e > nums[1]:
                return 0
            elif i == n - 1 and i > 0 and e > nums[i - 1]:
                return n - 1
            else:
                if nums[i - 1] < e > nums[i + 1]:
                    return i
        return 0


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        for i in range(n):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return 0
            elif i == n - 1:
                if nums[i] > nums[i-1]:
                    return n-1
            else:
                if nums[i-1] < nums[i] > nums[i+1]:
                    return i

        return -1

# https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode/


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 3, 1]))
    print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
