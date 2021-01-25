/*

https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

*/

package main


import "fmt"

// naive

/*
func isMatch(s string, p string) bool {
    var f func(s string, p string) bool
    f = func(s string, p string) bool {
        if len(p) == 0 {
            return len(s) == 0
        }
        if len(s) == 0 {
            if rune(p[0]) == '*' {
                return f(s, p[1:])
            }
            return false
        }
        if rune(p[0]) == '*' {
            return f(s[1:], p[1:]) || f(s, p[1:]) || f(s[1:], p)
        }
        if s[0] == p[0] || rune(p[0]) == '?' {
            return f(s[1:], p[1:])
        }
        return false
    }
    return f(s, p)
}
*/

// memo

/*
func isMatch(s string, p string) bool {
    dict := make(map[[2]int]bool)
    var f func(s string, p string) bool
    f = func(s string, p string) bool {
        m, n := len(s), len(p)
        key := [2]int{m, n}
        if v, ok := dict[key]; ok {
            return v
        }
        if n == 0 {
            return m == 0
        }
        if m == 0 {
            if rune(p[0]) == '*' {
                r := f(s, p[1:])
                dict[key] = r
                return r
            }
            dict[key] = false
            return false
        }
        if rune(p[0]) == '*' {
            r := f(s, p[1:]) || f(s[1:], p) || f(s[1:], p[1:])
            dict[key] = r
            return r
        }
        if s[0] == p[0] || rune(p[0]) == '?' {
            r := f(s[1:], p[1:])
            dict[key] = r
            return r
        }
        dict[key] = false
        return false
    }
    return f(s, p)
}
*/


func isMatch(s string, p string) bool {
    m, n := len(s), len(p)
    dp := make([][]bool, m+1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]bool, n + 1)
    }
    dp[m][n] = true
    for i := m; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            if rune(p[j]) == '*' {
                if i < m {
                    dp[i][j] = dp[i+1][j] || dp[i][j+1] || dp[i+1][j+1]
                } else {
                    dp[i][j] = dp[i][j+1]
                }
            } else if i < m && (s[i] == p[j] || rune(p[j]) == '?') {
                dp[i][j] = dp[i+1][j+1]
            }
        }
    }
    return dp[0][0]
}


// 凭借印象过了


func main() {
    s := "acdcb"
    p := "a*c?b"
    fmt.Println(isMatch(s, p))

    s = "aa"
    p = "*"
    fmt.Println(isMatch(s, p))

    s = "cb"
    p = "?a"
    fmt.Println(isMatch(s, p))

    s = "aa"
    p = "a"
    fmt.Println(isMatch(s, p))

    s = "adceb"
    p = "*a*b"
    fmt.Println(isMatch(s, p))

    s = "ab"
    p = "?*"
    fmt.Println(isMatch(s, p))

    s = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba"
    p = "a*******b"
    fmt.Println(isMatch(s, p))

}


