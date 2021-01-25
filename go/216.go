/*

https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

*/


package main


import "fmt"


func combinationSum3(k int, n int) [][]int {
    res := make([][]int, 0)
    var f func(k int, n int, pos int, buf []int)
    f = func(k int, n int, pos int, buf []int) {
        if n == 0 {
            if k == 0 {
                tmp := make([]int, len(buf))
                copy(tmp, buf)
                res = append(res, tmp)
                
            }
        }
        for i := pos; i <= 9; i++ {
            if i > n {
                break
            }
            buf = append(buf, i)
            f(k-1, n-i, i+1, buf)
            buf = buf[:len(buf) - 1]
        }
    }
    buf := make([]int, 0)
    f(k, n, 1, buf)
    return res
}


// 算是一道比较简单的组合排列题 


func main() {
    k := 3
    n := 7
    fmt.Println(combinationSum3(k, n))

    k = 3
    n = 9
    fmt.Println(combinationSum3(k, n))
}
