/*

https://leetcode.com/problems/combination-sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
*/


package main


import "fmt"
import "sort"


func combinationSum(candidates []int, target int) [][]int {
    sort.Ints(candidates)
    res := make([][]int, 0)
    var f func(buf []int, n int)
    f = func(buf []int, n int) {
        if n == 0 {
            tmp := make([]int, len(buf))
            copy(tmp, buf)
            res = append(res, tmp)
            return
        }
        for _, c := range candidates {
            if c > n {
                break
            }        
            // cut off
            // 非常经典的剪枝
            if len(buf) > 0 && buf[len(buf) - 1] > c {
                continue
            }
            buf = append(buf, c)
            f(buf, n - c)
            buf = buf[:len(buf) - 1]
        }
    }
    buf := make([]int, 0)
    f(buf, target)
    return res
}


func main() {
    candidates := []int{2,3,6,7}
    target := 7
    fmt.Println(combinationSum(candidates, target))
}
