/*

https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

*/

package main


import "fmt"


func max(nums ...int) int {
    r := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > r {
            r = nums[i]
        }
    }
    return r
}


func min(nums ...int) int {
    r := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] < r {
            r = nums[i]
        }
    }
    return r
}


func maxProduct(nums []int) int {
    N := len(nums)
    A := make([]int, N)
    B := make([]int, N)
    for i, e := range nums {
        if i == 0 {
            A[i] = e
            B[i] = e
        } else {
            a := A[i-1] * e
            b := B[i-1] * e
            // 虽然作对的 但是不知道为什么要这样做!!!
            A[i] = max(a, b, e)
            B[i] = min(a, b, e)
        }
    }
    return max(A...)
}


func main() {
    nums := []int{2,3,-2,4}
    fmt.Println(maxProduct(nums))

    nums = []int{-2, 0, -1}
    fmt.Println(maxProduct(nums))

    nums = []int{2,-5,-2,-4,3}
    fmt.Println(maxProduct(nums))
}
