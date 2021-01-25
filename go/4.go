/*

https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
*/


package main


func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}


func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    A, B, m, n := nums1, nums2, len(nums1), len(nums2)
    if m > n {
        A, B, m, n = B, A, n, m
    }
    imin, imax, half_len := 0, m, (m + n + 1) / 2
    for ;imin <= imax; {
        i := (imin + imax) / 2
        j := half_len - i
        if i < m && B[j - 1] > A[i] {
            imin = i + 1
        } else if i > 0 && A[i-1] > B[j] {
            imax = i - 1
        } else {
            max_of_left := 0
            min_of_right := 0
            if i == 0 {
                max_of_left = B[j-1]
            } else if j == 0 {
                max_of_left = A[i-1]
            } else {
                max_of_left = max(A[i-1], B[j-1])
            }
            if (m + n) & 1 != 0 {
                return float64(max_of_left)
            }
            if i == m {
                min_of_right = B[j]
            } else if j == n {
                min_of_right = A[i]
            } else {
                min_of_right = min(A[i], B[j])
            }
            return float64(max_of_left + min_of_right) / 2
        }
    }
    return 0.0
}


func main() {
    nums1 := []int{1,2}
    nums2 := []int{3,4}
    println(findMedianSortedArrays(nums1, nums2))

    nums1 = []int{1,3}
    nums2 = []int{2}
    println(findMedianSortedArrays(nums1, nums2))

}
