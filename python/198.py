"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(dp[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n-1] if n else 0

# 能够作对的最主要原因就是这道题比较简单啊


class Solution:
    """
    这是因为 重叠子问题 中的 问题i 只依赖于 i - 1, i - 2
    所以就用两个变量保存就可以了
    做题的方式应该是层层递进的
    不要一上来就希望得到最简单的结果
    因为中间的思考过程是省略不了的
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a, b, res = 0, nums[0], nums[0]
        for i in range(1, len(nums)):
            res = max(a + nums[i], b)
            a, b = b, res
        return res


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2, 7, 9, 3, 1]))

