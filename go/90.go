/*

https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
*/

package main


import "fmt"


import "sort"

func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums)

    res := make([][]int, 0)

    var f func(buf []int, pos int)
    f = func(buf []int, pos int) {
        // 在任意时间的添加!!!
        tmp := make([]int, len(buf))
        copy(tmp, buf) 
        res = append(res, tmp)
        for i := pos; i < len(nums); i++ {
            if i > pos && nums[i] == nums[i-1] {
                continue
            }
            buf = append(buf, nums[i])
            f(buf, i + 1)
            buf = buf[:len(buf) - 1]
        }
    }
    buf := make([]int, 0)
    f(buf, 0)
    return res
}


func main() {
    nums := []int{1,2,2}
    res := subsetsWithDup(nums)
    fmt.Println(res)
}
