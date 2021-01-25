/*

https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

*/


package main


import "fmt"


// very smart solution
func increasingTriplet(nums []int) bool {
    a, b := int((1 << 31) - 1), int((1 << 31) - 1)
    for i := 0; i < len(nums); i++ {
        n := nums[i]
        if n <= a {
            a = n
        } else if n <= b {
            b = n
        } else {
            return true
        }
    }
    return false
}


func main() {
    nums := []int{1,2,3,4,5}
    fmt.Println(increasingTriplet(nums))

    nums = []int{5,4,3,2,1}
    fmt.Println(increasingTriplet(nums))

    nums = []int{2147483646,2147483647,2147483647}
    fmt.Println(increasingTriplet(nums))
}
