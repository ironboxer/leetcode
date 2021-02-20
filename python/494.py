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



class Solution:
    """
    思路
这道题目咋眼一看和动态规划背包啥的也没啥关系。

本题要如何使表达式结果为target，

既然为target，那么就一定有 left组合 - right组合 = target。

left + right等于sum，而sum是固定的。

公式来了， left - (sum - left) = target -> left = (target + sum)/2 。

target是固定的，sum是固定的，left就可以求出来。

此时问题就是在集合nums中找出和为left的组合。


    这里的思路解释的很好
    原先的问题是需要数组中的每个元素都要参与
    而转化为01背包之后 只需要部分元素参与 得到解就可以了
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        # 不符合条件的情况
        if s < S or (s + S) & 1:
            return 0
        # 转化为01背包问题
        # 这里为什么可以转化为01背包问题呢?
        target = (s + S) >> 1
        total = len(nums)
        dp = [[0] * (target + 1) for _ in range(total + 1)]
        dp[0][0] = 1
        # 对于全部的物品 选择拿或者不难
        for i in range(0, total):
            # 对于每一种状态 探索在当前物品i拿或者不拿的情况下状态的变化情况
            for j in range(0, target+1):
                # 在可以放入的情况下 状态的变化情况
                if j >= nums[i]:
                    dp[i+1][j] = dp[i][j] + dp[i][j-nums[i]]
                # 在不能放入的情况下 状态的变化
                else:
                    dp[i+1][j] = dp[i][j]

        return dp[-1][-1]



# SLOW BUT WORK
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if s < S or (s + S) & 1:
            return 0

        target = (s + S) >> 1
        nums.sort()
        self.res = 0

        def f(pos, cur):
            if cur == target:
                self.res += 1

            if pos == len(nums):
                return

            for i in range(pos, len(nums)):
                if cur + nums[i] > target:
                    break
                f(i+1, cur + nums[i])


        f(0, 0)

        return self.res




from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if s < S or (s + S) & 1:
            return 0

        target = (s + S) >> 1
        nums.sort()

        @lru_cache
        def f(pos, cur):
            retval = 0

            if cur == target:
                retval += 1

            if pos == len(nums):
                return retval

            for i in range(pos, len(nums)):
                if cur + nums[i] > target:
                    break
                retval += f(i+1, cur + nums[i])

            return retval

        return f(0, 0)


# 回溯就是会超时啊 所以只能使用DP
# 而使用DP的前提就是将这个问题转化为01背包问题 然后套用01背包问题的模板就行了

from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if s < S or (s + S) & 1:
            return 0

        target = (s + S) >> 1
        nums.sort()

        @lru_cache
        def f(pos, cur):
            retval = 0

            if cur == 0:
                retval += 1

            if pos == len(nums):
                return retval

            for i in range(pos, len(nums)):
                if cur < nums[i]:
                    break
                retval += f(i+1, cur - nums[i])

            return retval

        return f(0, target)


