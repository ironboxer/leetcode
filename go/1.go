/*

https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

*/

package main

import "fmt"

func twoSum(nums []int, target int) []int {
    res := []int{-1, -1}
    dict := make(map[int]int)
    for i, e := range nums {
        idx, ok := dict[target -  e]
        if ok {
            res[0] = idx
            res[1] = i
            break
        }
        dict[e] = i
    }
    return res
}

// 字典的作用在于将时间复杂度从O(n^2)减小到O(n)
// golang programming language


func main() {
    nums := []int{2, 7, 11, 15}
    target := 13
    res := twoSum(nums, target)
    println(res[0], res[1])
    fmt.Println(nums)
}

