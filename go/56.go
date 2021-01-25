/*

https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.



Constraints:

intervals[i][0] <= intervals[i][1]

*/

package main


import "fmt"


import "sort"


type Interval struct {
    intervals [][]int
}

func (I *Interval) Len() int {
    return len(I.intervals)
}


func (I *Interval) Swap(i, j int) {
    I.intervals[i], I.intervals[j] = I.intervals[j], I.intervals[i]
}


func (I *Interval) Less(i, j int) bool {
    if I.intervals[i][0] == I.intervals[j][0] {
        return I.intervals[i][1] <= I.intervals[j][1]
    }
    return I.intervals[i][0] <= I.intervals[j][0]
}


func merge(intervals [][]int) [][]int {
    I := &Interval {intervals: intervals}
    sort.Sort(I)
    fmt.Println(intervals)
    res := make([][]int, 0)
    for _, e := range intervals {
        if len(res) == 0 {
            res = append(res, e)
        } else {
            if e[0] > res[len(res) - 1][1] {
                res = append(res, e)
            } else {
                if e[1] > res[len(res) - 1][1] {
                    res[len(res) - 1][1] = e[1]
                }
            }
        }
    }
    return res
}


func main() {
    intervals := [][]int{
        {1, 3},
        {2, 6},
        {8, 10},
        {15, 18},
    }
    // [1 3] 
    // [2 6]
    // [8 10]
    // [15 18]
    res := merge(intervals)
    fmt.Println(res)
    
    intervals = [][]int {
        {1, 4},
        {4, 5},
    }
    res = merge(intervals)
    fmt.Println(res)
}
