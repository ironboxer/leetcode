/*

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

*/


package main


import "fmt"


func findMin(nums []int) int {
    left, right := 0, len(nums) - 1
    for left < right {
        mid := (left + right) / 2
        if nums[left] <= nums[mid] && nums[mid] <= nums[right] {
            return nums[left]
        } else if nums[left] <= nums[mid] && nums[right] < nums[left] {
            left = mid + 1
        } else if nums[mid] <= nums[right] && nums[right] < nums[left] {
            right = mid 
        } else {
            left++
        }
    }
    return nums[left]
}

// 居然就蒙对了 不知道为什么

func main() {
    nums := []int{3,4,5,1,2}
    fmt.Println(findMin(nums))

    nums = []int{4,5,6,7,0,1,2}
    fmt.Println(findMin(nums))

    nums = []int{2, 1}
    fmt.Println(findMin(nums))

    nums = []int{1}
    fmt.Println(findMin(nums))

}

