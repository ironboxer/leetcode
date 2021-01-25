"""
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/

剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


限制：

0 <= 数组长度 <= 10^5



注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        for i in range(1, len(prices)):
            for j in range(i):
                r = max(r, prices[i] - prices[j])
        return r



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = len(prices)
        if total < 2:
            return 0
        res, min_val = 0, prices[0]
        for i in range(1, total):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                res = max(res, prices[i] - min_val)
        return res
