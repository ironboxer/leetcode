/*

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

*/

package main


import "fmt"


func search(nums []int, target int) bool {
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := left + (right - left) / 2
        if nums[mid] == target || nums[left] == target || nums[right] == target {
            return true
        } else if nums[left] <= target && target < nums[mid] {
            right = mid - 1
        } else if nums[mid] < target && target <= nums[right] {
            left = mid + 1
        } else {
            left++
            right--
        }
    }
    return false
}



func main() {
    nums := []int{2,5,6,0,0,1,2}
    target := 0
    fmt.Println(search(nums, target))


    target = 3
    fmt.Println(search(nums, target))


    nums = []int{1,3,1,1,1}
    target = 3
    fmt.Println(search(nums, target))
}


