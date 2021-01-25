/*

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9


*/

package main


import "fmt"


func left_search(nums []int, target int) int {
    hit := -1
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := left + (right - left) / 2
        if nums[mid] < target {
            left = mid + 1
        } else if nums[mid] > target {
            right = mid - 1
        } else {
            hit = mid
            right = mid - 1
        }
    }
    return hit
}


func right_search(nums[] int, target int) int {
    hit := -1
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := left + (right - left) / 2
        if nums[mid] < target {
            left = mid + 1
        } else if nums[mid] > target {
            right = mid - 1
        } else {
            hit = mid
            left = mid + 1
        }
    }
    return hit 
}

func searchRange(nums []int, target int) []int {
    if len(nums) == 0 {
        return []int{-1, -1}
    }
    return []int{left_search(nums, target), right_search(nums, target)}
}


func main() {
    nums := []int{5,7,7,8,8,10}
    target := 8
    fmt.Println(nums, target, searchRange(nums, target))

    target = 11
    fmt.Println(nums, target, searchRange(nums, target))


}

