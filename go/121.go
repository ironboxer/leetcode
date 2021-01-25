/*

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

*/

package main


import "fmt"


func max(a, b int) int  {
    if a >=b  {
        return a
    }
    return b
}

func maxProfit(prices []int) int {
    if len(prices) < 2 {
        return 0
    }
    profit := 0
    small := prices[0]
    for i := 1; i < len(prices);  i++ {
        if prices[i] > small {
            profit = max(profit, prices[i] - small)
        } else {
            small = prices[i]
        }
    }
    return profit
}


// 简单的需要仔细观察的题


func main() {
    //  [7,1,5,3,6,4]
    nums := []int{7,1,5,3,6,4}
    fmt.Println(maxProfit(nums))
}
