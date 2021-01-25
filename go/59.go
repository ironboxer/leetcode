/*

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
    row, col, counter, m, total := 0, 0, 1, n, n * n
    for counter <= total  {
        if row < m {
            for i := col; i < n; i++ {
                matrix[row][i] = counter
                counter++
            }
            row++
        }
        if col < n {
            for i := row; i < m; i++ {
                matrix[i][n-1] = counter
                counter++
            }
            n--
        } 
        if row < m {
            for i := n-1; i >= col; i-- {
                matrix[m-1][i] = counter
                counter++
            }
            m--
        }
        if col < n {
            for i := m-1; i >= row; i-- {
                matrix[i][col] = counter
                counter++
            }
            col++
        }
    }
    return matrix
}


func show(matrix [][]int) {
    for i := 0; i < len(matrix); i++ {
        fmt.Println(matrix[i])
    }
    fmt.Println()
}


func main() {
    for i := 0; i < 10; i++ {
        show(generateMatrix(i))
    }
}
