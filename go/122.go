/*

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

*/


package main


import "fmt"


func maxProfit(prices []int) int {
    if len(prices) < 2 {
        return 0
    }
    profit := 0
    // code block here
    for i := 0; i < len(prices); i++ {
        if i > 0 && prices[i] > prices[i-1] {
            profit = profit + (prices[i] - prices[i-1])
        }
    }
    return profit
}

// 上面这个解法 从含义上无法理解 但是从结果上 是等价的
// 这个问题可以被等价的转化为求连续和的问题


func main() {
    // [7,1,5,3,6,4]
    prices := []int{7,1,5,3,6,4}
    fmt.Println(maxProfit(prices))

    prices = []int{1, 5, 7}
    fmt.Println(maxProfit(prices))
}

