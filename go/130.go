/*

https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

*/

package main

import "fmt"


func solve(board [][]byte)  {
    if len(board) == 0 {
        return
    }
    m, n := len(board), len(board[0])
     
    var f func(i, j int)
    f = func(i, j int) {
        if i < 0 || j < 0 || i >= m || j >= n {
            return
        }
        if board[i][j] == 'O' {
            board[i][j] = '+'
            f(i+1, j)
            f(i-1, j)
            f(i, j+1)
            f(i, j-1)
        }
    }
    for i := 0; i < m; i++ {
        f(i, 0)
        f(i, n-1)
    }
    for i := 0; i < n; i++ {
        f(0, i)
        f(m-1, i)
    }
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if board[i][j] == 'O' {
                board[i][j] = 'X'
            }
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if board[i][j] == '+' {
                board[i][j] = 'O'
            }
        }
    }
}


// 绕弯子

/*
 X X X X
 X O O X
 X X O X
 X O X X
*/


/*

O O O
O O O
O O O

*/
func main() {
    board := [][]byte {
        {'X','X','X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'},
    }
    for _, row := range board {
        fmt.Println(row)
    }

    solve(board)

    for _, row := range board {
        fmt.Println(row)
    }
 
}
