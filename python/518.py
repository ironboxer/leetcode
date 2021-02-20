"""
https://leetcode.com/problems/coin-change-2/


518. Coin Change 2
Medium

2481

69

Add to List

Share
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
Accepted
158,316
Submissions
310,568
"""


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        res = []
        def f(amount, i, buf):
            if amount == 0:
                res.append(buf[:])
                return
            for j in range(i, len(coins)):
                c = coins[j]
                if c > amount:
                    break
                buf.append(c)
                f(amount - c, j, buf)
                buf.pop()

        f(amount, 0, [])
        print(res)
        return len(res)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        def f(amount, i):
            if amount == 0:
                return 1

            ans = 0
            for j in range(i, len(coins)):
                c = coins[j]
                if c > amount:
                    break
                ans += f(amount - c, j)
            return ans

        return f(amount, 0)


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pass



class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # 表示amount为0 result = 1
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(n):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    # 这里i+1的含义是可以重复选择元素 完全背包
                    # 如果改为i就是不能重复选择元素 普通背包 01背包
                    dp[i+1][j] = dp[i+1][j - coins[i]] + dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j]

        return dp[n][amount]



# TLE

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        res = []

        def f(cur, path):
            if cur == 0:
                res.append(path[:])
                return

            for c in coins:
                if c > cur:
                    break
                if path and c > path[-1]:
                    continue
                path.append(c)
                f(cur - c, path)
                path.pop()

        f(amount, [])

        return len(res)



class Solution:
    def change(self, amount: int, coins: List[int]) ->int:
        n = len(coins)
        dp = [1] + [0] * amount
        for i in range(n):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    # 完全背包
                    dp[j] += dp[j - coins[i]]
        return dp[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        total = len(coins)
        dp = [[0] * (amount + 1) for _ in range(total + 1)]
        for i in range(total+1):
            dp[i][0] = 1
        for i in range(total):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    # 这里 何时为 i 何时为i+1
                    # 这个问题的本质是完全背包问题 每个硬币可以使用多次
                    # 所以状态不需要从 dp[i][j-coins[i]]转移到dp[i+1][j]
                    # 而是从dp[i+1][j-coins[i]] 转移到dp[i+1][j]
                    # 这是非常重要的一点
                    dp[i+1][j] = dp[i+1][j-coins[i]] + dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j]

        return dp[-1][-1]



class Solution:
    """
    问题 什么是状态压缩 什么情况下可以使用状态压缩
    """
    def change(self, amount: int, coins: List[int]) -> int:

        total = len(coins)
        dp = [1] + [0] * amount
        for i in range(total):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[j] += dp[j-coins[i]]

        return dp[-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        total = len(coins)
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(1, amount+1):
                if j >= coin:
                    dp[j] += dp[j-coin]

        return dp[amount]



if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))

    amount = 2
    coins = [1]
    print(Solution().change(amount, coins))

    amount = 3
    coins = [2]
    print(Solution().change(amount, coins))

    amount = 10
    coins = [10]
    print(Solution().change(amount, coins))

    amount = 500
    coins = [3,5,7,8,9,10,11]
    print(Solution().change(amount, coins))

