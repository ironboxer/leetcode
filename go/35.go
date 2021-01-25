/*

https://leetcode.com/problems/search-insert-position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

*/


package main


import "fmt"


func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := left + (right - left) / 2
        if nums[mid] < target {
            left = mid + 1
        } else if nums[mid] > target {
            right = mid - 1
        } else {
            return mid
        }
    }
    return left
}

// 二分查找的变形

func main() {
    nums := []int{1,3,5,6}
    for i := 0; i < 10; i++ {
        fmt.Println(nums, i, searchInsert(nums, i))
    }
}
