/*

https://leetcode.com/problems/summary-ranges/

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

*/


package main


import "fmt"
import "strconv"


func summaryRanges(nums []int) []string {
    res := make([]string, 0)
    n := len(nums)
    if n == 0 {
        return res
    }
    last := nums[0]
    for i := 1; i < n; i++ {
        if nums[i] != nums[i-1] + 1 {
            if nums[i-1] == last {
                res = append(res, strconv.Itoa(last))
            } else {
                res = append(res, strconv.Itoa(last) + "->" +  strconv.Itoa(nums[i-1]))
            }
            last = nums[i]
        }
    }
    if nums[n-1] == last {
        res = append(res, strconv.Itoa(last))
    } else {
        res = append(res, strconv.Itoa(last) + "->" +  strconv.Itoa(nums[n-1]))
    }
    return res
}


// 没有什么特殊的算法 仔细观察总结就可以了
// 可能会考察临场的能力


func main() {
    nums := []int{0,1,2,4,5,7}
    fmt.Println(summaryRanges(nums))

    nums = []int{1,2,3,4}
    fmt.Println(summaryRanges(nums))

    nums = []int{1,2,3,5,7,8,9,10}
    fmt.Println(summaryRanges(nums))

    nums = []int{1}
    fmt.Println(summaryRanges(nums))

    nums = []int{1,2,4,5,7,8}
    fmt.Println(summaryRanges(nums))

}

