/*

https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647


Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

*/


package main


import "fmt"


func maxSubArray(nums []int) int {
    if len(nums) < 1 {
        return 0
    }
    max := nums[0]
    for i := 1; i < len(nums); i++ {
        // 一个十分简单而巧妙的思路
        if nums[i-1] > 0 {
            nums[i] = nums[i] + nums[i-1]
        }
        if nums[i] > max {
            max = nums[i]
        }
    }
    return max
}


func main() {
    nums := []int{-2,1,-3,4,-1,2,1,-5,4}
    fmt.Println(nums)
    fmt.Println(maxSubArray(nums))
    fmt.Println(nums)
}
