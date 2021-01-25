/*

https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


你所有的不懂都在这
https://zh.wikipedia.org/wiki/%E5%85%AB%E7%9A%87%E5%90%8E%E9%97%AE%E9%A2%98

*/

package main


import "fmt"
import "strings"


/*
最难懂的地方
其实是没人解释

*/
func validate(board [][]string, x int, y int) bool {
    for i := 0; i < len(board); i++ {
        for j := 0; j < y; j++ {
            // 判断的方向
            // x == i 同一行
            // x + j == y + i 对角线
            // x + y == i + j 斜对角线
            if board[i][j] == "Q" && (x + j == y + i || x + y == i + j || x == i) {
                return false
            }
        }
    }
    return true
}


func construct(board [][]string) []string {
    res := make([]string, len(board))
    for i := 0; i < len(board); i++ {
        res[i] = strings.Join(board[i], "")
    }
    return res
}


func dfs(board [][]string, colIndex int, res *[][]string) {
    if colIndex == len(board) {
       *res = append(*res, construct(board))
       return
    }
    for i := 0; i < len(board); i++ {
        if validate(board, i, colIndex) {
            board[i][colIndex] = "Q"
            dfs(board, colIndex + 1, res)
            board[i][colIndex] = "."
        }
    }
}


func solveNQueens(n int) [][]string {
    board := make([][]string, n)
    for i := 0; i < n; i++ {
        board[i] = make([]string, n)
        for j := 0; j < n; j++ {
            board[i][j] = "."
        }
    }
    res := make([][]string, 0)
    dfs(board, 0, &res)
    return res
}


func main() {
    for i := 4; i < 9; i++ {
        res := solveNQueens(i)
        fmt.Println(i)
        for _, board  := range res {
            for _, row := range board {
                fmt.Println(row)
            }
            fmt.Println()
        }
        fmt.Println("\n\n")
    }
}
