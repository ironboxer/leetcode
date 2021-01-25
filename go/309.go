/*

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

*/

package main


import "fmt"


func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


// 还是太抽象了 看不懂
// FSM 有限状态机
// 不是简单的理解既可以会的
func maxProfit(prices []int) int {
    free, have, cool := 0, -999999, -999999
    for _, p := range prices {
        free, have, cool = max(free, cool), max(have, free - p), have + p
        fmt.Println(free, have, cool)
    }
    return max(free, cool)
}


func main() {
    prices := []int{1,2,3,0,2}
    fmt.Println(maxProfit(prices))
}

