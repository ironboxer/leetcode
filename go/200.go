/*

https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

*/

package main


import "fmt"


func numIslands(grid [][]byte) int {
    m, n := len(grid), len(grid[0])
    var f func(i, j int)
    f = func(i, j int) {
        if i < 0 || j < 0 || i >= m || j >= n {
            return
        } 
        if grid[i][j] == '1' {
            grid[i][j] = '0'
            f(i+1, j)
            f(i-1, j)
            f(i, j+1)
            f(i, j-1)
        }
    }
    res := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == '1' {
                res++
                f(i, j)
            }
        }
    }
    return res
}


func main() {
    grid := [][]byte {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'},
    }
    fmt.Println(numIslands(grid))

    grid = [][]byte {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'},
    }
    fmt.Println(numIslands(grid))
}
