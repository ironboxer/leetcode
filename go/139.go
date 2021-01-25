/*

https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

*/


package main


import "fmt"
//import "strings"

/*
func wordBreak(s string, wordDict []string) bool {
    memo := make(map[string]bool)
    var f func(str string) bool
    f = func(str string) bool {
        if len(str) == 0 {
            return true
        }
        val, ok := memo[str]
        if ok {
            return val
        }
        for _, w := range wordDict {
            if strings.HasPrefix(str, w) {
                r := f(str[len(w):])
                if r {
                    memo[str] = true
                    return true
                }
            }
        }
        memo[str] = false
        return false
    }
    return f(s)
}
*/


func wordBreak(s string, wordDict []string) bool { 
    N := len(s)
    dp := make([]bool, N + 1)
    dp[0] = true
    for i := 0; i < N; i++ {
        // 这点非常关键 否则后面就是在做无用功
        if !dp[i] {
            continue
        }
        for _, w := range wordDict {
            if i + len(w) <= N && s[i:i + len(w)] == w {
                dp[i + len(w)] = dp[i]
            }
        } 
    }
    //fmt.Println(dp)
    return dp[N]
}
 

// 因为是一维数组 所以比较简单



func main() {
    s := "leetcode"
    wordDict := []string{"leet", "code"}
    fmt.Println(wordBreak(s, wordDict))

    s = "applepenapple"
    wordDict = []string{"apple", "pen"}
    fmt.Println(wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = []string{"cats", "dog", "sand", "and", "cat"}
    fmt.Println(wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = []string{"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}
    fmt.Println(wordBreak(s, wordDict))

    
    s = "abcd"
    wordDict =[]string{"a","abc","b","cd"}
    fmt.Println(wordBreak(s, wordDict))
    
    s = "aaaaaaa"
    wordDict = []string{"aaaa","aaa"}
    fmt.Println(wordBreak(s, wordDict))
}


