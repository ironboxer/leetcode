/*

https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

*/


package main


import "fmt"


func max(nums ...int) int {
    r := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > r {
            r = nums[i]
        }
    }
    return r
}


func rob(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    if len(nums) == 1 {
        return nums[0]
    }
    f := func(nums []int) int {
        dp := make([]int, len(nums) + 1)
        for i := 0; i < len(nums); i++ {
            if i == 0 {
                dp[i+1] = nums[0]
            } else {
                dp[i+1] = max(dp[i], dp[i-1] + nums[i])
            }
        }
        return max(dp...)
    }
    // 这是一个很巧妙地方法
    return max(f(nums[1:]), f(nums[:len(nums) - 1]))
}



func main() {
    nums := []int{1,2,3,1}
    fmt.Println(rob(nums))

    nums = []int{2,3,2}
    fmt.Println(rob(nums))

}
