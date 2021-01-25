/*

https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

*/


package main


import "fmt"


// 这道题读完之后没有任何的感觉 说明 还是大脑中没有建立响应的模型
// 读完之后没有任何的感觉啊
// 就是简单地几行代码的问题 但是如果想不到 就完全没有思路
// 而思路 是要多思考 多做题得出来的


func maxSlidingWindow(nums []int, k int) []int {
    res := make([]int, 0)
    queue := make([]int, 0)
    for i, e := range nums {
        for len(queue) > 0 && nums[queue[len(queue) - 1]] < e {
            queue = queue[:len(queue) - 1]
        }
        if len(queue) > 0 && queue[0] + k <= i {
            queue = queue[1:]
        }
        queue = append(queue, i)
        if i >= k - 1 {
            res = append(res, nums[queue[0]])
        }
    }
    return res
}


func main() {
    nums := []int{1,3,-1,-3,5,3,6,7}
    k := 3
    fmt.Println(maxSlidingWindow(nums, k))
}

