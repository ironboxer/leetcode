/*

https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5

*/

package main


import "fmt"


func canJump(nums []int) bool {
    max := 0
    for i, e := range nums {
        if i + e > max {
            max = i + e
        }
        if max + 1 >= len(nums) {
            return true
        }
        // 神奇的补刀
        if max == i {
            return false
        }
    }
    return false
}


func main() {
    nums := []int{2,3,1,1,4}
    fmt.Println(nums, canJump(nums))

    nums = []int{3,2,1,0,4}
    fmt.Println(nums, canJump(nums))

    nums = []int{2, 0}
    fmt.Println(nums, canJump(nums))

    nums = []int{3,2,1,0,4}
    fmt.Println(nums, canJump(nums))
}
