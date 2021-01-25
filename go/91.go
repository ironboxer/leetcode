/*

https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

*/

package main


import "fmt"


func numDecodings(s string) int {
    if len(s) == 0 || s[0] == 48 {
        return 0
    }
    n := len(s)
    dp := make([]int, n + 1)    
    dp[0] = 1
    // 确实是很好的解法 需要仔细体会一下
    for i := 0; i < n; i++ {
        // i != 0
        if (s[i] - 48) > 0 {
            dp[i+1] += dp[i]
        }
        // 10 <= s[i-1:i+1] <= 26
        if i > 0 && 10 <= (s[i-1] - 48) * 10 + (s[i] - 48) && (s[i-1] - 48) * 10 + (s[i] - 48) <= 26 {
            dp[i+1] += dp[i-1]
        }
    }    
    fmt.Println(dp)
    return dp[n]
}


// 古老而经典的做法


func main() {
    s := "226"
    fmt.Println(numDecodings(s))

    s = "1234"
    fmt.Println(numDecodings(s))

    s = "12120"
    fmt.Println(numDecodings(s))

    s = "10"
    fmt.Println(numDecodings(s))
}

