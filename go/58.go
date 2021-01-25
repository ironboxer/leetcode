/*

https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

*/

package main


import "fmt"


func generateMatrix(n int) [][]int {
    matrix := make([][]int, n)
    for i := 0; i < n; i++ {
        matrix[i] = make([]int, n) 
    }
    counter, total := 1, n * n
    row, col := 0, 0
    maxRow, maxCol := n, n
    for counter <= total {
        if row < maxRow {
            for i := col; i < maxCol; i++ {
                matrix[row][i] = counter
                counter++
            }
            row++
        }
        if col < maxCol {
            for i := row; i < maxRow; i++ {
                matrix[i][maxCol-1] = counter
                counter++
            }
            maxCol--
        }
        if row < maxRow {
            for i := maxCol - 1; i >= col; i-- {
                matrix[maxRow-1][i] = counter
                counter++
            }
            maxRow--
        }
        if col < maxCol {
            for i := maxRow - 1; i >= row; i-- {
                matrix[i][col] = counter
                counter++
            }
            col++
        }
    }
    return matrix
}


func main() {
    for i := 2; i < 10; i++ {
        matrix := generateMatrix(i)
        for _, row := range matrix {
            fmt.Println(row)
        }
        fmt.Println("\n\n")
    }
}
