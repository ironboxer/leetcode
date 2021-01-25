/*

https://leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.


Example:

Input: [2,1,5,6,2,3]
Output: 10

*/


package main


import "fmt"


func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


func largestRectangleArea(heights []int) int {
    if len(heights) == 0 {
        return 0
    }
    stack := make([]int,  0)
    length := len(heights)
    max_area := 0
    for i := 0; i < length; i++ {
        for len(stack) > 0 && heights[i] < heights[stack[len(stack) - 1]] {
            pos := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            area := 0
            if len(stack) == 0 {
                area = heights[pos] * i
            } else {
                area = heights[pos] * (i - stack[len(stack) - 1] - 1)
            }
            max_area = max(max_area, area)
        }
        stack = append(stack, i)
    }
    for len(stack) > 0 {
        pos := stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        area := 0
        if len(stack) == 0 {
            area = heights[pos] * length
        } else {
            area = heights[pos] * (length - stack[len(stack) - 1] - 1)
        }
        max_area = max(max_area, area)
    }
    return max_area
}


func main() {
    heights := []int{2,1,5,6,2,3}
    fmt.Println(largestRectangleArea(heights))
}

