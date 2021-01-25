/*

https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

*/


package main


import "fmt"
import "sort"


func combinationSum2(candidates []int, target int) [][]int {
    sort.Ints(candidates)    
    res := make([][]int, 0)
    var f func(buf []int, pos int, n int)
    f = func(buf []int, pos int, n int) {
        if n == 0 {
            tmp := make([]int, len(buf))
            copy(tmp, buf)
            res = append(res, tmp)
            return
        }
        for i := pos; i < len(candidates); i++ {
            e := candidates[i]
            if e > n {
                break
            }
            // 这是最关键的一步
            if i > pos && e == candidates[i-1] {
                continue
            }
            buf = append(buf, e)
            f(buf, i + 1, n - e)
            buf = buf[:len(buf) - 1]
        }
    }
    buf := make([]int, 0)
    f(buf, 0, target)
    return res
}


func main() {
    candidates := []int{10,1,2,7,6,1,5}
    target := 8
    fmt.Println(combinationSum2(candidates, target))
}


