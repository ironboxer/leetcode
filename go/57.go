/*

https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


*/


package main


import "fmt"


func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}


func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


func insert(intervals [][]int, newInterval []int) [][]int {
    res := make([][]int, 0)
    i := 0
    // left most part
    for i < len(intervals) && intervals[i][1] < newInterval[0] {
        res = append(res, intervals[i])
        i++
    }
    // merge range
    // newInterval 是被实时更新的
    for i < len(intervals) && intervals[i][0] <= newInterval[1] {
        newInterval = []int {
            min(newInterval[0], intervals[i][0]),
            max(newInterval[1], intervals[i][1]),
        }
        i++
    }
    res = append(res, newInterval)
    // right most part
    res = append(res, intervals[i:]...)
    return res
}


func main() {
    intervals := [][]int {
        {1, 3},
        {6, 9},
    }
    newInterval := []int {
        2, 5,
    }
    fmt.Println(intervals, newInterval)
    res := insert(intervals, newInterval)
    fmt.Println(res)
   
    intervals = [][]int {
        {1, 2},
        {3, 5},
        {6, 7},
        {8, 10},
        {12, 16},
    }

    newInterval = []int {
        4, 8,
    }
    fmt.Println(intervals, newInterval)
    res = insert(intervals, newInterval)
    fmt.Println(res)

    intervals = [][]int{
        {1, 2},
    }

    newInterval = []int {
        3, 4,
    }
    fmt.Println(intervals, newInterval)
    res = insert(intervals, newInterval)
    fmt.Println(res)

    intervals = [][]int {
        {1, 2},
        {3, 5},
        {6, 7},
        {8, 10},
        {12, 16},
    }

    newInterval = []int {
        4, 8, 
    }
    fmt.Println(intervals, newInterval)
    res = insert(intervals, newInterval)
    fmt.Println(res)
}
