/*
https://leetcode-cn.com/problems/longest-valid-parentheses/

32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。



示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0


提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'

*/



package main

import "fmt"


func max(nums... int) int {
    var retval = 0
    for _, e := range nums {
        if e > retval {
            retval = e
        }
    }
    return retval
}

// 发现自己确实不会 因为连问题的基本定义都没有搞清楚
// (  ) ( (  ) )
// 0  2 0 0  2 6
func longestValidParentheses(s string) int {
    var total = len(s)
    if total < 2 {
        return 0
    }
    var dp = make([]int, total)
    for i := 1; i < total; i++ {
        if s[i] == ')' {
            if s[i-1] == '(' {
                // ()()
                if i > 2 {
                    dp[i] = 2 + dp[i-2]
                } else {
                    dp[i] = 2
                }
            } else {
                // ()(())
                // 012345
                // dp[5-1] > 0 && 5 - dp[4]   - 1 >= 0
                if dp[i-1] > 0 && i - 1 - dp[i-1] >= 0 && s[i - 1 - dp[i-1]] == '(' {
                    if i - 2 - dp[i-1] > 0 {
                        dp[i] = 2 + dp[i-1] + dp[i - 2 - dp[i-1]]
                    } else {
                        dp[i] = 2 + dp[i-1]
                    }
                }
            }
        }
    } 

    fmt.Println(dp)

    return max(dp...)
}


func main() {
    var s = "()(())"
    var r = longestValidParentheses(s)
    fmt.Println(s, r)
}

