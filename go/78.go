/*

https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

*/


package main


import "fmt"


func subsets(nums []int) [][]int {
    res := make([][]int, 1) 
    res[0] = make([]int, 0) 
    for i := 0; i < len(nums); i++ {
        buf := make([][]int, 0)
        for j := 0; j < len(res); j++ {
            items := res[j]
            tmp := make([]int, len(items) + 1)
            copy(tmp, items)
            tmp[len(items)] = nums[i]
            buf = append(buf, tmp)
        }
        res = append(res, buf...)
    }
    return res
}


func main() {
    nums := []int{1,2, 3}
    fmt.Println(subsets(nums))
}
