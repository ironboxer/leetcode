"""
https://leetcode-cn.com/problems/coin-lcci/


面试题 08.11. 硬币
硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

示例1:

 输入: n = 5
 输出：2
 解释: 有两种方式可以凑成总金额:
5=5
5=1+1+1+1+1
示例2:

 输入: n = 10
 输出：4
 解释: 有四种方式可以凑成总金额:
10=10
10=5+5
10=5+1+1+1+1+1
10=1+1+1+1+1+1+1+1+1+1
说明：

注意:

你可以假设：

0 <= n (总金额) <= 1000000

"""


class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        dp = [1] + [0] * n
        for c in coins:
            for i in range(c, n + 1):
                dp[i] += dp[i-c]

        return dp[n] % 1000000007



# SLOW BUT WORK

class Solution:
    def waysToChange(self, n: int) -> int:
        coins = (1, 5, 10, 25)

        def f(pos, amount):
            if amount == 0:
                return 1
            if pos == 4:
                return 0
            retval = 0
            for i in range(pos, 4):
                if coins[i] > amount:
                    break
                # 注意 这里的i很重要 需要保持 求和的序列是一个递增的序列
                # 因为这道题本质上是在求解 硬币的组合数 而不是排列数
                # 所以需要 放置重复的序列出现
                # 这里的i 其实是last index的意思
                # 保证后续加入的元素>= last index
                # 这样来保证该序列
                retval += f(i, amount - coins[i])
            return retval

        return f(0, n) % 1000000007


###

class Solution:
    def waysToChange(self, n: int) -> int:
        coins = (1, 5, 10, 25)

        dp = [1] + [0] * n
        # 这里如果两层for循环的位置改变 得到的结果就是不一样的
        # 其中 一个是组合的结果 一个是排列的结果
        # 组合排列 他们很相似 但是结果不一样
        for c in coins:
            for i in range(1, n+1):
                if i >= c:
                    dp[i] += dp[i-c]
        return dp[-1] % 1000000007




class Solution:
    def waysToChange(self, n: int) -> int:
        coins = (1, 5, 10, 25)
        dp = [[0] * (n + 1) for _ in range(5)]
        for i in range(5):
            dp[i][0] = 1
        for i in range(4):
            for j in range(1, n+1):
                if j >= coins[i]:
                    # 状态转移方程写不出来 就要写代码
                    # 结果就是这样啊
                    # 这里的状态转移方程式基于物品的 而不是 钱数
                    # 所以这里发生变动的两个值分别是 i <- i - 1, j <- j - coins[i]
                    # 这样才是正确的 而不是 j <- j - 1 这个有什么实际的意义吗
                    # 根本没有
                    dp[i+1][j] = dp[i+1][j-coins[i]] + dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j]

        return dp[-1][-1] % 1000000007


if __name__ == '__main__':
    for i in range(1, 11):
        print(i, Solution().waysToChange(i))


