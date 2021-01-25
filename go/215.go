/*

https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

*/


package main


import "fmt"


func partation(nums []int, left, right int) int {
    pivot := nums[left]
    for left <= right {
        for left <= right && nums[left] < pivot {
            left++
        }
        for left <= right && nums[right] > pivot {
            right--
        }
        if left <= right {
            nums[left], nums[right] = nums[right], nums[left]
            left++
            right--
        }
    }
    return left
}


func quickSelect(nums []int, k int) int {
    left, right := 0, len(nums) - 1
    for left < right {
        pivot := partation(nums, left, right)
        if pivot > k {
            right = pivot - 1
        } else if pivot <= k {
            left = pivot
        }
    }
    return left
}


func quickSort(nums []int, left, right int) {
    if left < right {
        pivot := partation(nums, left, right)
        quickSort(nums, left, pivot - 1)
        quickSort(nums, pivot, right)
    }
}


func findKthLargest(nums []int, k int) int {
    pos := quickSelect(nums, len(nums) - k)
    return nums[pos]
}


func main() {
    nums := []int{3,2,1,5,6,4} 
    k := 2
    nums2 := make([]int, len(nums))
    copy(nums2, nums)
    quickSort(nums2, 0, len(nums2) - 1)
    fmt.Println(nums2, k, nums2[len(nums2) - k])
    fmt.Println(findKthLargest(nums, k))

    nums = []int{3,2,3,1,2,4,5,5,6}
    k = 4
    nums2 = make([]int, len(nums))
    copy(nums2, nums)
    quickSort(nums2, 0, len(nums2) - 1)
    fmt.Println(nums2, k, nums2[len(nums2) - k])
    fmt.Println(findKthLargest(nums, k))
}
