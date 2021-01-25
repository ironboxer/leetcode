/*

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

*/


package main


import "fmt"



func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}


func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


// 你能看得懂吗
func maxProfit(prices []int) int {
    sell1, sell2 := 0, 0
    buy1, buy2 := int((2 << 30) - 1), int((2 << 30) - 1)
    for _, p := range prices {
        // 第一次买入的最小化费
        buy1  = min(buy1, p)
        // 第一次卖出的最大收益
        sell1 = max(sell1, p - buy1)
        // 第二次买入的最小化费
        buy2  = min(buy2, p - sell1)
        // 第二次卖出的最大收益
        sell2 = max(sell2, p - buy2)
    }
    return sell2
}


// golang 的测试结果为甚磨如此的不稳定?


func main() {
    // prices = [3,3,5,0,0,3,1,4]
    prices := []int{3,3,5,0,0,3,1,4}
    fmt.Println(maxProfit(prices))
}

