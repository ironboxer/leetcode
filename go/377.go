/*

https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

*/


package main



import "fmt"



/*
func combinationSum4(nums []int, target int) int {
    res := 0
    var f func(val int)
    f = func(val int) {
        if val == 0 {
            res++
            return
        }
        for _, e := range nums {
            if e > val {
                continue
            }
            f(val - e)
        }
    }
    f(target)
    return res
}
*/


import "sort"



/*
// 递归是符合自然逻辑的方法
// memorize 是一种优化
func combinationSum4(nums []int, target int) int {
    if len(nums) == 0 {
        return 0
    }
    sort.Ints(nums)
    memo := make(map[int]int)
    var f func(val int) int
    f = func(val int) int {
        if val == 0 {
            return 1  
        }
        if val < nums[0] {
            return 0
        }
        res, ok := memo[val]
        if ok {
            return res
        }
        res = 0
        for _, e := range nums {
            if e > val {
                break
            }
            r := f(val - e) 
            if r > 0 {
                res = res + r
            }
        }
        memo[val] = res
        return res
    }
    return f(target)
}
*/


/*
func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}
*/


func combinationSum4(nums []int, target int) int {
    if len(nums) == 0 {
        return 0
    }
    sort.Ints(nums)
    dp := make([]int, target + 1)
    dp[0] = 1
    for i := 1; i < target + 1; i++ {
        for _, n := range nums {
            if n > i {
                break
            }
            //dp[i] = max(dp[i], dp[i - n] + 1)
            dp[i] = dp[i] + dp[i - n]
        }
    }
    return dp[target]
}


func main() {
    nums := []int{1, 2, 3}
    fmt.Println(combinationSum4(nums, 4))

    nums = []int{2, 1, 3}
    fmt.Println(combinationSum4(nums, 35))

    nums = []int{9}
    fmt.Println(combinationSum4(nums, 3))
}
