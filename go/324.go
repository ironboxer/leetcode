/*

https://leetcode.com/problems/wiggle-sort-ii/

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

*/

package main


import "fmt"
import "sort"


// 虽然不符合题意 但是能做对
func wiggleSort(nums []int)  {
    sort.Ints(nums)    
    total := len(nums)
    half := (total + 1) / 2
    arr := make([]int, total)
    copy(arr, nums)
    i, j := half - 1, total - 1
    for k := 0; k < total; k++ {
        if k % 2 == 0 {
            nums[k] = arr[i]
            i--
        } else {
            nums[k] = arr[j]
            j--
        }
    }
}


func main() {
    nums := []int{1, 5, 1, 1, 6, 4}
    fmt.Println(nums)
    wiggleSort(nums)
    fmt.Println(nums)

    nums = []int{1, 3, 2, 2, 3, 1}
    fmt.Println(nums)
    wiggleSort(nums)
    fmt.Println(nums)
}
