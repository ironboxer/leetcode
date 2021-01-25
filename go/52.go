/*

https://leetcode.com/problems/n-queens-ii/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

*/

package main


import "fmt"



func validate(board [][]string, row int, col int) bool {
    for i := 0; i < len(board); i++ {
        for j := 0; j < col; j++ {
            if board[i][j] == "Q" {
                if row + j == col + i || row + col == i + j || row == i {
                    return false
                }
            }
        }
    }
    return true
}


func dfs(board [][]string, col int, total *int) {
    if col == len(board) {
        *total = *total + 1
        return
    }
    for row := 0; row < len(board); row++ {
        if validate(board, row, col)  {
            board[row][col] = "Q"
            dfs(board, col + 1, total)
            board[row][col] = "."
        }
    }
}


func totalNQueens(n int) int {
    board := make([][]string, n)
    for i := 0; i < n; i++ {
        board[i] = make([]string, n)
        for j := 0; j < n; j++ {
            board[i][j] = "."
        }
    }

    var total int = 0
    dfs(board, 0, &total)
    return total
}

// 这个虽然跑得慢 但是容易理解 理解才能够应用
// 其他的版本稍微复杂有点 理解起来有点麻烦

func main() {
    for i := 4; i < 10; i++ {
        fmt.Println(i, totalNQueens(i))
    }
}
