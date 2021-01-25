/*

https://leetcode.com/problems/sudoku-solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

*/


package main


import "fmt"


func check(board [][]byte, row int, col int, d byte) bool {
    for i := 0; i < 9; i++ {
        // board[i][j] == '.' 说明当前这个位置还未放置元素 所以应该跳过
        // check each row at position i
        if rune(board[i][col]) != '.' && board[i][col] == d {
            return false
        }
        // check each column at position i
        if rune(board[row][i]) != '.' && board[row][i] == d {
            return false
        }
        // check skew line
        // 这个地方的判断有点trick
        if rune(board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3]) != '.' && board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == d {
            return false
        }
    }
    return true
}


func solve(board [][]byte) bool {
    digits := []byte{'1','2','3','4','5','6','7','8','9'}
    for i := 0; i < len(board); i++ {
        for j := 0; j < len(board[i]); j++ {
            // . 的位置是用来放置的位置
            if rune(board[i][j]) == '.' {
                for _, d := range digits {
                    if check(board, i, j, d) {
                        board[i][j] = d
                        if solve(board) {
                            return true
                        } else {
                            board[i][j] = '.'
                        }    
                    }                 
                }
                return false
            }
        }
    }
    return true
}


func solveSudoku(board [][]byte){
    if len(board) == 0 {
        return
    }
    solve(board)
}


func main() {
    board := [][]byte {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'},
    }

    fmt.Println(board)
    solveSudoku(board)
    fmt.Println(board)
}

