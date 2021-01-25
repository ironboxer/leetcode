
/*

https://leetcode.com/problems/word-search/description/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

*/


package main


import "fmt"


func exist(board [][]byte, word string) bool {
    m, n, r := len(board), len(board[0]), len(word)
    var f func(i, j, k int) bool
    f = func(i, j, k  int) bool {
        if k == r {
            return true
        }
        if i < 0 || i >= m || j < 0 || j >= n {
            return false
        }
        if board[i][j] != word[k] {
            return false
        }
        t := board[i][j]
        board[i][j] = '*'
        res := f(i+1, j, k+1) || f(i-1, j, k+1) || f(i, j+1, k+1) || f(i, j-1, k+1)
        board[i][j] = t
        return res
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if board[i][j] == word[0] && f(i, j, 0) {
                return true
            }
        }
    }
    return false
}


func main() {
    board := [][]byte {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'},
    } 
    word := "ABCCED"
    fmt.Println(exist(board, word))

    word = "SEE"
    fmt.Println(exist(board, word))

    word = "ABCB"
    fmt.Println(exist(board, word))

}
