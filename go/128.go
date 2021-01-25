/*

https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

*/


package main


import "fmt"


func longestConsecutive(nums []int) int {
    if len(nums) == 0 {
        return  0
    }

    dict := make(map[int]bool) 
    for i := 0; i < len(nums); i++ {
        dict[nums[i]] = true
    }
    total := 1
    for i := 0; i < len(nums); i++ {
        cur := 1
        _, ok := dict[nums[i] - 1]
        if ok {
            continue
        }
        j := nums[i] + 1
        // 最长的序列只会遍历一遍 O(2n)
        for {
            _, ok := dict[j]
            if !ok {
                break
            }
            j++
            cur++
        }
        if cur > total {
            total = cur
        }
    }
    return total
}

// 这是一个非常巧妙的算法

func main() {
    nums := []int{100, 4, 200, 1, 3, 2}
    fmt.Println(longestConsecutive(nums))

    nums = []int{5,4,3,2,1}
    fmt.Println(longestConsecutive(nums))
}
