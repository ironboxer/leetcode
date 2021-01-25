/*

https://leetcode.com/problems/distinct-subsequences/

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It's guaranteed the answer fits on a 32-bit signed integer.


Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^


Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
abgbag
  ^  ^^
babgbag
    ^^^

*/


package main


import "fmt"


/*
func numDistinct(s string, t string) int {
    memo := make(map[[2]int]int)
    var f func(s, t string) int
    f = func(s, t string) int {
        if len(t) == 0 {
            return 1
        }
        if len(s) == 0 {
            return 0
        }
        key := [2]int{len(s), len(t)}
        v, ok := memo[key]
        if ok {
            return v
        }
        if s[len(s) - 1] == t[len(t) - 1] {
            v = f(s[:len(s) - 1], t) + f(s[:len(s) - 1], t[:len(t) - 1])
        } else {
            v = f(s[:len(s) - 1], t)
        } 
        memo[key] = v
        return v
    }  
    return f(s, t)
}
*/


// 很简答的思路
// 代码很简单 但是不懂为什么要这样?


func numDistinct(s string, t string) int {
    m, n := len(t), len(s)
    dp := make([][]int, m + 1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]int, n + 1)
    }
    // t = ''
    for i := 0; i < n + 1; i++ {
        dp[0][i] = 1
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if t[i] == s[j] {
                dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
            } else {
                dp[i+1][j+1] = dp[i+1][j]
            }
        }
    }
    return dp[m][n]
}

// 需要一些时间理解
func main() {
    s := "babgbag"
    t := "bag"
    fmt.Println(s, t, numDistinct(s, t))

    s = "rabbbit"
    t = "rabbit"
    fmt.Println(s, t, numDistinct(s, t))
}

