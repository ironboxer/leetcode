/*

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

*/


package main


import "fmt"

import "sort"


func min(a, b int) int {
    if a <= b  {
        return a
    }
    return b
}


/*
// 这类简单的动态规划

func coinChange(coins []int, amount int) int {
    memo := make(map[int]int)
    var f func(n int) int
    f = func(n int) int {
        if n == 0 {
            return 0
        }
        r, ok := memo[n]
        if ok {
            return r
        }
        r = 999999
        for i := 0; i < len(coins); i++ {
            coin := coins[i]
            if coin <= n {
                t := f(n - coin) + 1
                r = min(r, t)
            }
        }
        memo[n] = r
        return r
    }
    r := f(amount)
    if r < 999999 {
        return r
    }
    return -1
}
*/


func coinChange(coins []int, amount int) int {
    sort.Ints(coins)
    dp := make([]int, amount + 1)
    for i := 1; i < amount + 1; i++ {
        dp[i] = 999999
    }
    for i := 1; i < amount + 1; i++ {
        for j := 0; j < len(coins); j++ {
            coin := coins[j]
            if coin > i {
                break
            }
            dp[i] = min(dp[i], dp[i - coin] + 1)
        }
    }
    if dp[amount] >= 999999 {
        return -1
    }
    return dp[amount]
}


func main() {
    coins := []int{1, 2, 5}
    amount := 11
    fmt.Println(coinChange(coins, amount))

    coins = []int{2}
    amount = 3
    fmt.Println(coinChange(coins, amount))


    coins = []int{1}
    amount = 0
    fmt.Println(coinChange(coins, amount))

    coins = []int{1,2,5}
    amount = 100
    fmt.Println(coinChange(coins, amount))


    coins = []int{2,5,10,1}
    amount = 27
    fmt.Println(coinChange(coins, amount))

}
