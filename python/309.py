"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)

"""


from typing import List

class Solution:
    """
    free is the maximum profit I can have while being free to buy.
    have is the maximum profit I can have while having stock.
    cool is the maximum profit I can have while cooling down.
    """
    def maxProfit(self, prices: List[int]) -> int:
        free = 0
        have = cool = -999999
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
            print('price: %d, free: %d, have: %d, cool: %d' % (p, free, have, cool))
        return max(free, cool)


class Solution:
    """
    用动态规划来模拟状态之间的迁移
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        s0, s1, s2 = [0] * n, [0] * n, [0] * n
        s1[0] = -prices[0]
        s2[0] = -(1 << 31)
        for i in range(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]

        return max(s0[-1], s2[-1])



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # cooldown -2day
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[n-1][0]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = dp[-1][1] - prices[0]

        for i in range(1, n):
            # 0 1 分别表示手上没有/有股票 + prices[i]表示在当前的价格prices[i]出手
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # -prices[i]表示入手当前的股票 -2表示在入手之前一定要空一天
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        return dp[n-1][0]


if __name__ == '__main__':
    prices = [1,2,3,0,2]
    print(prices, Solution().maxProfit(prices))
    prices = [1, 2]
    print(prices, Solution().maxProfit(prices))

    prices = [2, 1, 4]
    print(prices, Solution().maxProfit(prices))


