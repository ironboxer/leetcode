/*

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

*/


package main


import "fmt"


func findMin(nums []int) int {
    left, right := 0, len(nums) - 1
    for left < right {
        mid := (left + right) / 2
        if nums[mid] > nums[right] {
            left = mid + 1 
        // nums[right] <= nums[left]
        } else if nums[mid] < nums[left] {
            right = mid
            // nums[right] <= nums[left]
            left++
        } else {
            // 这一步是耗时的
            right--
        }
    }
    return nums[left]
}


func main() {
    nums := []int{1,2,3}
    fmt.Println(findMin(nums))

    nums = []int{2,2,2,0,1}
    fmt.Println(findMin(nums))

    nums = []int{3,3,1,3}
    fmt.Println(findMin(nums))

    nums = []int{1}
    fmt.Println(findMin(nums))

    nums = []int{2, 1}
    fmt.Println(findMin(nums))
}
