"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105

"""

# 建立直觉上的联系

from typing import List


class Solution:
    """
    说明当时没看懂
    看懂了就不是这种表述了
    """
    def maxProfit(self, prices: List[int]) -> int:
        sell1, sell2, buy1, buy2 = 0, 0, -999999, -999999
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
            print(buy1, sell1, buy2, sell2)
        return sell2


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell1, sell2 = 0, 0
        buy1, buy2 = float('inf'), float('inf')
        for p in prices:
            # 第一次买入的最小化费
            buy1 = min(buy1, p)
            # 第一次卖出的最大收益
            sell1 = max(sell1, p - buy1)
            # 第二次买入的最小化费
            buy2 = min(buy2, p - sell1)
            # 第二次卖出的最大收益
            sell2 = max(sell2, p - buy2)
            print(buy1, sell1, buy2, sell2)
        return sell2






class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        K = 2
        dp = [[[0, 0] for _ in range(K+1)] for _ in range(n)]
        # 这个地方是试出来的
        for k in range(1, K+1):
            dp[0][k][1] = -prices[0]

        for i in range(1, n):
            for k in range(1, K+1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[n-1][K][0]



if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
    print(Solution().maxProfit([7,6,4,3,1]))
    print(Solution().maxProfit([2, 1, 4]))


