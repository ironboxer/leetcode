/*

https://leetcode.com/problems/perfect-squares/


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

*/

package main


import "fmt"


func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}



/*
func numSquares(n int) int {
    dict := make(map[int]int)
    var f func(n int) int
    f = func(n int) int {
        if n == 0 {
            return 0
        }
        if n == 1 {
            return 1
        }
        v, ok := dict[n]
        if ok {
            return v
        }
        v = 999999
        for i := 1; i * i <= n; i++ {
            v = min(v, f(n - i * i))
        }
        dict[n] = v + 1
        return v + 1
    }
    return f(n)
}
*/



// 简单的动态规划应用
func numSquares(n int) int {
    dp := make([]int, n + 1)
    dp[1] = 1
    for i := 2; i < n + 1; i++ {
        dp[i] = 999999
    }
    for i := 2; i <= n; i++ {
        for j := 1; j * j <= i; j++ {
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        }
    }
    return dp[n]
}


func main() {
    for i := 1; i < 20; i++ {
        fmt.Println(i, numSquares(i))
    }
}

