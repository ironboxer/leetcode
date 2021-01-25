/*

https://leetcode.com/problems/trapping-rain-water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

*/


package main


import "fmt"


func trap(height []int) int {
    res := 0
    max_left_h, max_right_h := 0, 0
    left, right := 0, len(height) - 1
    for left < right {
        if height[left] <= height[right] {
            if height[left] > max_left_h {
                max_left_h = height[left]
            } else {
                res = res + (max_left_h - height[left])
                left++
            }
        } else {
            if height[right] > max_right_h {
                max_right_h = height[right]
            } else {
                res = res + (max_right_h - height[right])
                right--
            }
        }
    }
    return res
}

// 多想几个例子 仔细体会这种解法的好处
// 作者也不是一下子就想到的


func main() {
    height := []int{0,1,0,2,1,0,1,3,2,1,2,1}
    fmt.Println(trap(height))
}

