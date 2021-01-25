"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        first = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < first:
                right = mid - 1
            else:
                left = mid + 1
        # 这个也是可行的 边界条件是 left == N 也是只想最后一个元素
        return nums[left % len(nums)]


# 这道题就这么混过去了, 为什么对了也不知道

# 又一种新的思路
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid
            else:
                break

        return nums[left]


# 总是能昏过去
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        l, r, p = 0, len(nums), nums[0]
        while l < r:
            m = (l + r) // 2
            if nums[m] >= p:
                l = m + 1
            else:
                r = m
        return nums[r]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            # 一定在右侧出现了翻转
            if nums[m] > nums[r]:
                l = m + 1
            # 一定在左侧出现了翻转
            elif nums[m] < nums[l]:
                r = m
            else:
                break

        return nums[l]


#多思考


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5, 1, 2]))
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
    print(Solution().findMin([1]))

