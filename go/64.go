/*

https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

*/


package main


import "fmt"


func min(a, b int) int  {
    if a <= b {
        return a
    }
    return b
}


func minPathSum(grid [][]int) int {
    if len(grid) < 0 {
        return 0
    }
    m, n := len(grid), len(grid[0])
    dp := make([][]int, m)
    for i := 0; i < m; i++ {
        dp[i] = make([]int, n)
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i == 0 && j == 0 {
                dp[i][j] = grid[i][j]
            } else if i == 0 {
                dp[i][j] = grid[i][j] + dp[i][j-1]
            } else if j == 0 {
                dp[i][j] = grid[i][j] + dp[i-1][j]
            } else {
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
            }
        }
    }
    return dp[m-1][n-1]
}


func main() {
    grid := [][]int {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1},
    }
    fmt.Println(minPathSum(grid))
}
