"""
https://leetcode-cn.com/problems/target-sum/


494. 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。



示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。


提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。
"""


from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0

        def f(i, s):
            if i == len(nums):
                if s == 0:
                    self.res += 1
                return

            f(i+1, s - nums[i])
            f(i+1, s + nums[i])

        f(0, S)

        return self.res



class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if S > s:
            return 0
        if (s + S) & 1:
            return 0
        x = (s + S) >> 1
        dp = [0] * (x + 1)
        dp[0] = 1

        for n in nums:
            for i in range(x, n-1, -1):
                dp[i] += dp[i - n]

        return dp[x]


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if S > s:
            return 0
        if (s + S) & 1:
            return 0
        x = (s + S) >> 1
        total = len(nums)
        dp = [[0] * (x + 1) for _ in range(total + 1)]
        dp[0][0] = 1
        for i in range(0, total):
            for j in range(0, x+1):
                if j < nums[i]:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] + dp[i][j-nums[i]]

        return dp[total][x]



