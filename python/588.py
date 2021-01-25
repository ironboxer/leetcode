"""
https://leetcode.com/problems/coin-change-2/

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
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][amount]


# 可以使用搜索 但是更好的方法是动态规划
# 动态规划的两个关键点 1 状态 2 选择
# 表格就是记录在不同的状态下 不同的选择的结果


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))

    amount = 3
    coins = [2]
    print(Solution().change(amount, coins))

    amount = 10
    coins = [10]
    print(Solution().change(amount, coins))



