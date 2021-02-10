"""
https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

"""


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n + 1) * n // 2
        for e in nums:
            s -= e
        return s

# XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 根据题意
        missing = len(nums)
        for i, e in enumerate(nums):
            # 异或满足交换律
            # 交换意味着延时
            missing = missing ^ (i ^ e)
        return missing


if __name__ == '__main__':
    print(Solution().missingNumber([3,0,1]))
    print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))

