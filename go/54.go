/*

https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

*/

package main


import "fmt"


func spiralOrder(matrix [][]int) []int {
    if len(matrix) == 0 {
        return []int{}
    }
    m, n := len(matrix), len(matrix[0])
    row, col, total := 0, 0, m * n

    res := make([]int, 0)
    for len(res) < total {
        if row < m {
            for i := col; i < n; i++ {
                res = append(res, matrix[row][i])
            }
            row++
        }
        if col < n {
            for i := row; i < m; i++ {
                res = append(res, matrix[i][n-1])
            }
            n--
        }
        if row < m {
            for i := n-1; i >= col; i-- {
                res = append(res, matrix[m-1][i])
            }
            m--
        }
        if col < n {
            for i := m-1; i >= row; i-- {
                res = append(res, matrix[i][col])
            }
            col++
        }
    }
    return res
}


func main() {
    nums := [][]int {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
    }
    for _, row  := range nums {
        fmt.Println(row)
    }
    r := spiralOrder(nums)
    fmt.Println(r)
}

