"""
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        # 用一个临时变量来保存
        t = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= t
            t *= nums[i]
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([24,12,8,6]))


