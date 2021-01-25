"""
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i, e in enumerate(nums):
            if e != 0:
                nums[p] = e
                p += 1
        while p < len(nums):
            nums[p] = 0
            p += 1


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print(nums)
    Solution().moveZeroes(nums)
    print(nums)
