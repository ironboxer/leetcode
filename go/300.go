/*

https://leetcode.com/problems/longest-increasing-subsequence/


Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


public class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int len = 0;
        for (int num : nums) {
            int i = Arrays.binarySearch(dp, 0, len, num);
            if (i < 0) {
                i = -(i + 1);
            }
            dp[i] = num;
            if (i == len) {
                len++;
            }
        }
        return len;
    }
}

*/


package main


import "fmt"


/*
func max(nums ...int) int {
    r := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > r {
            r = nums[i]
        }
    }
    return r
}


func lengthOfLIS(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    dp := make([]int, len(nums) + 1) 
    for i := 1; i < len(nums); i++ {
        for j := 0; j < i; j++ {
            if nums[j] < nums[i] {
                dp[i] = max(dp[i], dp[j] + 1)
            }
        }
    }
    return max(dp...) + 1
}
*/


// bisect_left 要找到元素应该插入的位置

func bsearch(nums []int, left, right, target int) int {
    for left < right {
        mid := (left + right) / 2
        if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}


// 这是一个很好的思路 时刻保持一个最长子序列的数组 来比较大小
func lengthOfLIS(nums []int) int {
    dp := make([]int, len(nums))
    maxLen := 0
    for i := 0; i < len(nums); i++ {
        e := nums[i]
        // 在已经有序的数组中找到属于自己的位置
        j := bsearch(dp, 0, maxLen, e)
        fmt.Println(dp[0: maxLen + 1], e, j)
        if j < 0 {
            j = -(j + 1)
        }
        dp[j] = e
        if j == maxLen {
            maxLen++
        }
    }
    return maxLen
}


func main() {
    nums := []int{10,9,2,5,3,7,101,18}
    fmt.Println(lengthOfLIS(nums))
    
    nums = []int{-2, -1}
    fmt.Println(lengthOfLIS(nums))
}

