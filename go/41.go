/*

https://leetcode.com/problems/first-missing-positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

*/


package main

import "fmt"


func firstMissingPositive(nums []int) int {
    total := len(nums)
    for i := 0; i < total; {
        e := nums[i]
        flag := true
        for 0 < e && e <= total && nums[e - 1] != e {
            //fmt.Println("before", e, nums)
            nums[e - 1], nums[i] = nums[i], nums[e - 1]
            //fmt.Println("after", e, nums)
            flag = false
        }
        if flag {
            i++
        }
    }
    for i := 0; i < total; i++ {
        if nums[i] != i + 1 {
            return i + 1
        }
    }
    return total + 1
}


func main() {
    nums := []int{7,8,9,11,12}
    fmt.Println(nums, firstMissingPositive(nums))

    nums = []int{1,2,0}
    fmt.Println(nums, firstMissingPositive(nums))
    
    nums = []int{3,4,-1,1}
    fmt.Println(nums, firstMissingPositive(nums))

    nums = []int{}
    fmt.Println(nums, firstMissingPositive(nums))


}
