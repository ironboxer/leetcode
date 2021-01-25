/*

https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

*/

package main


import "fmt"



func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}


func intersect(nums1 []int, nums2 []int) []int {
    A, B := make(map[int]int), make(map[int]int)
    for _, e := range nums1 {
        v, ok := A[e]
        if !ok {
            v = 0
        }
        A[e] = v + 1
    }
    for _, e := range nums2 {
        v, ok := B[e]
        if !ok {
            v = 0
        }
        B[e] = v + 1
    }
    if len(B) < len(A) {
        A, B = B, A
    }
    res := make([]int, 0)
    for key, v1 := range A {
        v2, ok := B[key]
        if ok {
            v := min(v1, v2)
            for v > 0 {
                res = append(res, key)
                v--
            }
        }
    }
    return res
}


func main() {
    nums1 := []int{1,2,2,1}
    nums2 := []int{2,2}
    fmt.Println(intersect(nums1, nums2))

    nums1 = []int{4,9,5}
    nums2 = []int{9,4,9,8,4}
    fmt.Println(intersect(nums1, nums2))

}
