/*
fmt.Println(nums, jump(nums))

https://leetcode.com/problems/jump-game-ii

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

*/


package main


import "fmt"


func jump(nums []int) int {
    total := len(nums)
    steps, maxReach, lastReach := 0, 0, 0
    for i, e := range nums {
        if lastReach + 1 >= total {
            break
        }
        if i > lastReach {
            lastReach = maxReach
            steps++
        }
        if i + e > maxReach {
            maxReach = i + e
        }
    }
    return steps
}


// 你看懂了吗?


func main() {
    nums := []int{2,3,1,1,4}
    fmt.Println(nums, jump(nums))

    nums = []int{1}
    fmt.Println(nums, jump(nums))

    nums = []int{0}
    fmt.Println(nums, jump(nums))

    nums = []int{7,0,9,6,9,6,1,7,9,0,1,2,9,0,3}
    fmt.Println(nums, jump(nums))
}
