/*

https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
*/


package main


import "fmt"



func min(nums ...int) int {
    r := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] < r {
            r = nums[i]
        }
    }
    return r
}


func max(nums ...int) int {
    r := nums[0]
     for i := 1; i < len(nums); i++ {
         if nums[i] > r {
             r = nums[i]
         }
     }
     return r
}


func maximalSquare(matrix [][]byte) int {
    if len(matrix) == 0 {
        return 0
    }
    m, n := len(matrix), len(matrix[0])
    dp := make([][]int, m + 1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]int, n + 1)
    }
    r := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if matrix[i][j] == '1' {
                // 这是最关键的地方
                // 状态转移方程:
                // 符合矩阵边长的定义
                // f(i, j) = min(f(i-1, j-1), f(i-1, j), f(i, j-1)) + 1
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
            } else {
                dp[i+1][j+1] = 0
            }
            r = max(r, dp[i+1][j+1])
        }
    }
    fmt.Println(dp)
    return r * r
}


// 动态规划石门艺术


func main() {
    matrix := [][]byte {
        {'1', '0', '1',  '0', '0'},
        {'1', '0', '1',  '1', '1'},
        {'1', '1', '1',  '1', '1'},
        {'1', '0', '0',  '1', '0'},
    }
    fmt.Println(maximalSquare(matrix))

    matrix = [][]byte {
        {'1', '1'},
        {'1', '1'},
    }
    fmt.Println(maximalSquare(matrix))

    matrix = [][]byte {
        {'1', '1'},
    }
    fmt.Println(maximalSquare(matrix))
}
