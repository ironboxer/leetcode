/*

https://leetcode.com/problems/regular-expression-matching/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

*/

package main

/*
func isMatch(s string, p string) bool {
    if len(s) == 0 && len(p) == 0 {
        return true
    }
    if len(p) == 0 {
        return false
    }
    if len(s) == 0 {
        if p[0] == '*' {
            return isMatch(s, p[1:])
        }
        if len(p) > 1 && p[1] == '*' {
            return isMatch(s, p[2:])
        }
        return false
    }
    if len(p) > 1 && p[1] == '*' {
        if s[0] == p[0] || p[0] == '.' {
            return isMatch(s, p[2:]) || isMatch(s[1:], p[2:]) || isMatch(s[1:], p)
        }
        return isMatch(s, p[2:]) 
    }
    if s[0] == p[0] || p[0] == '.' {
        return isMatch(s[1:], p[1:])
    }
    return false
}
*/

/*
func f(s string, p string, i int, j int) bool {
    m, n := len(s), len(p)
    if j == n {
        return i == m
    }
    cond := false
    if i < m && (s[i] == p[j] || p[j] == '.') {
        cond = true
    }
    if j + 1 < n && p[j+1] == '*' {
        if cond {
            return f(s, p, i, j + 2) || f(s, p, i + 1, j) || f(s, p, i + 1, j + 2)
        }
        return f(s, p, i, j + 2)
    }
    if cond {
        return f(s, p, i + 1, j + 1)
    }
    return false
}
*/



/*
func f(s string, p string, i int, j int, memo map[[2]int]bool) bool {
    key := [2]int{i, j} 
    val, ok := memo[key]
    if ok {
        return val
    }
    m, n := len(s), len(p)
    if j == n {
        return i == m
    }
    cond := false
    if i < m && (s[i] == p[j] || p[j] == '.') {
        cond = true
    }
    if j + 1 < n && p[j+1] == '*' {
        if cond {
            val = f(s, p, i, j + 2, memo) || f(s, p, i + 1, j, memo) || f(s, p, i + 1, j + 2, memo)
            memo[key] = val
            return val
        }
        val = f(s, p, i, j + 2, memo)
        memo[key] = val
        return val
    }
    if cond {
        val = f(s, p, i + 1, j + 1, memo)
        memo[key] = val
        return val
    }
    memo[key] = false
    return false
}

func isMatch(s string, p string) bool {
    memo := make(map[[2]int]bool)
    return f(s, p, 0, 0, memo)
}
*/


func isMatch(s string, p string) bool {
    m, n := len(s), len(p)
    dp := make([][]bool, m + 1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]bool, n + 1)
    }
    // s p 都是空串的情况下应该设置为true
    dp[m][n] = true
    // i 从m开始,是为了配合dp[i][j] = dp[i][j+2] 比如: s = '' p = 'a*' 应该要匹配上
    for i := m; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            cond := false
            if i < m && (s[i] == p[j] || p[j] == '.') {
                cond = true
            }
            if j + 1 < n && p[j+1] == '*' {
                if cond {
                    dp[i][j] = dp[i][j+2] || dp[i+1][j] || dp[i+1][j+2]
                } else {
                    dp[i][j] = dp[i][j+2]
                }
            } else if cond {
                dp[i][j] = dp[i+1][j+1]
            }
        }
    }
    // 因为top down 的版本是 从 0,0 到m,n 所以 buttom up的版本正好反过来
    return dp[0][0]
}


func main() {
    s := "mississippi"
    p := "mis*is*p*."
    println(s, p, isMatch(s, p))

    s = "aab"
    p = "c*a*b"
    println(s, p, isMatch(s, p))

    s = "ab"
    p = ".*"
    println(s, p, isMatch(s, p))

    s = "aa"
    p = "a*"
    println(s, p, isMatch(s, p))

    s = "aa"
    p = "a"
    println(s, p, isMatch(s, p))

    s= "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*c"
    println(s, p, isMatch(s, p))

}
