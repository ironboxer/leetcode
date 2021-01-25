/*

https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

*/


package main


import "fmt"


// 一个很实用的小技巧
func productExceptSelf(nums []int) []int {
    dp := make([]int, len(nums))
    dp[0] = 1
    // 累计从做向右的积
    for i := 1; i < len(nums); i++ {
        dp[i] = dp[i-1] * nums[i - 1]
    }
    // 累计从右向左的积
    r := nums[len(nums) - 1]
    for i := len(dp) - 2; i >= 0; i-- {
        dp[i] = dp[i] * r
        r = r * nums[i]
    }
    return dp
}


func main() {
    nums := []int{1,2,3,4}
    fmt.Println(nums)
    fmt.Println(productExceptSelf(nums))
}

