/*

https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

*/

package main


import "fmt"


func containsDuplicate(nums []int) bool {
    dict := make(map[int]bool)
    for i := 0; i < len(nums); i++ {
        _, ok := dict[nums[i]]
        if ok {
            return true
        }
        dict[nums[i]] = true
    }
    return false
}



// 有啥意思呢?

/*
func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}


func containsDuplicate(nums []int) bool {
    total := len(nums)
    var pos uint = 0
    var neg uint = 0
    for i := 0; i < total; i++ {
        n := nums[i]
        var mask uint = 1 << uint(abs(n))
        if n >= 0 {
            if pos & mask != 0 {
                return true
            } else {
                pos = pos ^ mask
            }
        } else {
            if neg & mask != 0 {
                return true
            } else {
                neg = neg ^ mask
            }
        }
    }
    return false
} 

*/ 

func main() {
    nums := []int{1,1,1,3,3,4,3,2,4,2}
    fmt.Println(containsDuplicate(nums))

    nums = []int{1,2,3,1}
    fmt.Println(containsDuplicate(nums))

    nums = []int{1,2,3}
    fmt.Println(containsDuplicate(nums))

    nums = []int{-1200000005,-1200000005}
    fmt.Println(containsDuplicate(nums))
}
