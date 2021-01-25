/*

https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

*/

package main


import "fmt"


func minSubArrayLen(s int, nums []int) int {
    N := len(nums)
    if N == 0 {
        return 0
    }
    res := 0
    j := 0
    cur := 0
    for i := 0; i < N; i++ {
        cur = cur + nums[i]
        for cur >= s {
            dist := i - j + 1
            if res == 0 {
                res = dist
            } else if dist < res{
                res = dist
            }
            cur = cur - nums[j]   
            j++
        }
    }
    return res
}


// sliding window


func main() {
    nums :=[]int{2,3,1,2,4,3}
    s := 7
    fmt.Println(minSubArrayLen(s, nums))

    nums = []int{1,2,3,4,5}
    s = 15
    fmt.Println(minSubArrayLen(s, nums))

    nums = []int{5,1,3,5,10,7,4,9,2,8}
    s = 15
    fmt.Println(minSubArrayLen(s, nums))

    nums = []int{1,2,3}
    s = 10
    fmt.Println(minSubArrayLen(s, nums))
}
