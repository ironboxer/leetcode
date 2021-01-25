/*

https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

*/


package main


import "fmt"


func permute(nums []int) [][]int {
    res := make([][]int, 0)
    var f func(pos int)
    f = func(pos int) {
        if pos == len(nums) {
            tmp := make([]int, len(nums))
            copy(tmp, nums)
            res = append(res, tmp)
            return
        }
        for i :=pos; i < len(nums); i++ {
            nums[i], nums[pos] = nums[pos], nums[i]
            f(pos+1)
            nums[i], nums[pos] = nums[pos], nums[i]
        }
    }
    f(0)
    return res
}


func main() {
    nums := []int{1,2,3}
    fmt.Println(permute(nums))
}
