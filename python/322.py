"""
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

"""

from typing import List


class Solution0:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def f(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            buf = [f(n - c) for c in coins if n >= c]
            r = min(buf) + 1 if buf else 999999
            memo[n] = r
            return r

        t = f(amount)
        return t if t < 999999 else -1


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {}
        def f(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            buf = [f(n - c) for c in coins if n >= c]
            r = min(buf) + 1 if buf else 999999
            memo[n] = r
            return r

        t = f(amount)
        return t if t < 999999 else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] + [999999] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if c > i:
                    break
                dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] < 999999 else -1



























class Solution:
    """
    理解题意
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [0] + [999999] * amount
        for a in range(1, amount + 1):
            for c in coins:
                if c > a:
                    break
                dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] < 999999 else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))

    coins = [2]
    amount = 3
    print(Solution().coinChange(coins, amount))

    coins = [1]
    amount = 0
    print(Solution().coinChange(coins, amount))

    coins = [1]
    amount = 1
    print(Solution().coinChange(coins, amount))

    coins = [1]
    amount = 2
    print(Solution().coinChange(coins, amount))

    coins = [2,5,10, 1]
    amount = 27
    print(Solution().coinChange(coins, amount))

    coins = [186,419,83,408]
    amount = 6249
    print(Solution().coinChange(coins, amount))


