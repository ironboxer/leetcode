/*

https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n

*/


package main


import "fmt"


func merge(nums1 []int, m int, nums2 []int, n int)  {
    p := m + n - 1
    i, j := m - 1, n - 1
    for i >= 0 && j >= 0 {
        if nums1[i] >= nums2[j] {
            nums1[p] = nums1[i]
            i--
        } else {
            nums1[p] = nums2[j]
            j--
        }
        p--
    }
    for i >= 0 {
        nums1[p] = nums1[i]
        i--
        p--
    }

    for j >= 0 {
        nums1[p] = nums2[j]
        j--
        p--
    }
}


func main() {
    nums1 := []int{1,2,3,0,0,0}
    m := 3
    nums2 := []int{2,5,6}
    n := 3

    fmt.Println(nums1, nums2)
    merge(nums1, m, nums2, n)    
    fmt.Println(nums1)

    nums1 = []int{0}
    nums2 = []int{1}
    m = 0
    n = 1
    fmt.Println(nums1, nums2)
    merge(nums1, m, nums2, n)    
    fmt.Println(nums1)

}
