/*
https://leetcode.com/problems/russian-doll-envelopes/

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

*/


package main


import "fmt"
import "sort"


type Matrix [][]int

func (m Matrix) Len() int {
    return len(m)
}


func (m Matrix) Less(i, j int) bool {
    if m[i][0] == m[j][0] {
        return -m[i][1] < -m[j][1]
    }
    return m[i][0] < m[j][0]
}


func (m Matrix) Swap(i, j int) {
    m[i], m[j] = m[j], m[i]
}


func less(A, B []int) bool {
    if A[0] < B[0] && A[1] < B[1]  {
        return true
    }
    return false
}


func bisect_left(nums [][]int, target []int) int {
    left, right := 0, len(nums)
    for left < right {
        mid := left + (right - left) / 2
        if less(nums[mid], target) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}




func maxEnvelopes(envelopes [][]int) int {
    mat := Matrix(envelopes)
    sort.Sort(mat)
    fmt.Println(envelopes)
    buf := make([][]int, 0)
    for _, n := range envelopes {
        pos := bisect_left(buf, n)
        if pos < len(buf) {
            buf[pos] = n
        } else {
            buf = append(buf, n)
        }
    }
    fmt.Println(buf)
    return len(buf)
}



func main() {
    envelops := [][]int {
        {5, 4},
        {6, 4},
        {6, 7},
        {2, 3},
    }
    fmt.Println(maxEnvelopes(envelops))

    envelops = [][]int {
        {1, 3},
        {3, 5},
        {6, 7},
        {6, 8},
        {8, 4},
        {9, 5},
    }
    fmt.Println(maxEnvelopes(envelops))
}
