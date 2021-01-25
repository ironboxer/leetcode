/*

https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

*/


package main


import "fmt"


func moveZeroes(nums []int)  {
    p := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[p] = nums[i]
            p++
        } 
    }
    for i := p; i < len(nums); i++ {
        nums[i] = 0
    }
}

func main() {
    nums := []int{0,1,0,3,12}
    fmt.Println(nums)
    moveZeroes(nums)
    fmt.Println(nums)
}
