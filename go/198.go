/*

https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

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
    n := len(nums)
    dp := make([]int, n+1)    
    for i := 0; i < n; i++ {
        if i == 0 {
            dp[i + 1] = max(dp[i], nums[i])
        } else {
            dp[i + 1] = max(dp[i], dp[i-1] + nums[i])
        }
    }
    return max(dp...)
}


// 因为状态转移方程太简单了

// f(i) = max{f(i-1), f(i-2) + nums[i]}

// 瞎猫碰到死耗子

func main() {
    nums := []int{1,2,3,1}
    fmt.Println(rob(nums))

    nums = []int{2,7,9,3,1}
    fmt.Println(rob(nums))
}

