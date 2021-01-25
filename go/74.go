/*

https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

*/


package main

import "fmt"


func searchMatrix(matrix [][]int, target int) bool {
    if len(matrix) == 0 {
        return false
    }
    m, n := len(matrix), len(matrix[0])
    i, j := 0, n - 1
    for i < m && j >= 0 {
        if matrix[i][j] < target {
            i++
        } else if matrix[i][j] > target {
            j--
        } else {
            return true
        }
    }
    return false
}

func main() {
    matrix := [][]int {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 50},
    }
    target := 3
    fmt.Println(searchMatrix(matrix, target))
}
