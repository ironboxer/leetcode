"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            max(nums)

        def f(nums):
            total = len(nums)
            dp = [0] * (total + 1)
            for i, e in enumerate(nums):
                if i == 0:
                    dp[i+1] = e
                else:
                    dp[i+1] = max(dp[i-1] + e, dp[i])
            return dp[total]

        return max(f(nums[:-1]), f(nums[1:]))


class Solution:
    """
    相对于原来的题198
    只是一个简单的变形
    """
    def rob(self, nums: List[int]) -> int:

        def f(nums):
            if not nums:
                return 0
            a, b, res = 0, nums[0], nums[0]
            for i in range(1, len(nums)):
                # 这个地方的替换和斐波那契数列一样
                # 只是每次递增的值不一样
                res = max(a + nums[i], b)
                a, b = b, res
            return res

        return max(f(nums[1:]), f(nums[:-1])) if len(nums) > 1 else sum(nums)


if __name__ == '__main__':
    print(Solution().rob([2,3,2]))
    print(Solution().rob([1,2,3,1]))

