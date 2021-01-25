/*

https://leetcode.com/problems/search-in-rotated-sorted-array

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

*/


package main


import "fmt"


func search(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right {
        mid := left + (right - left) / 2
        //println(nums[left], nums[mid], nums[right], target)
        if nums[mid] == target {
            return mid
        } else if nums[left] <= target && target < nums[mid] {
            right = mid - 1
        } else if nums[mid] < target && target <= nums[right] {
            left = mid + 1
        } else if target < nums[mid] && nums[mid] <= nums[right] {
            right = mid - 1
        } else if nums[left] <= nums[mid] && nums[mid] < target {
            left = mid + 1
        } else {
            if target < nums[left] {
                left++
            } else if target > nums[right] {
                right--
            }
            /*
            if nums[mid] <= nums[right] && nums[right] < target {
                right = mid - 1
            } else if target <= nums[left] && nums[left] < nums[mid] {
                left = mid + 1
            } else {
                println("here")
                left++
                right--
            }
            */
        }
    }
    return -1
}


// 稀里糊涂就过了 还是属于二分查找的变种


func main() {
    nums := []int{7, 9, 11, 13, 15, 1, 3, 5}
    fmt.Println(nums)
    for i := 0; i < 20; i++ {
        fmt.Println(i, search(nums, i))
    } 

    nums = []int{3,2}
    fmt.Println(nums, search(nums, 1))
    fmt.Println(nums, search(nums, 4))
    
    nums = []int{3, 1}
    fmt.Println(nums, search(nums, 1))

}
