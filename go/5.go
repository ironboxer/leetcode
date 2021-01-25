/*

https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

*/

package main


/*
这个解法比较简单而且直接 但就是想不到啊
*/
func longestPalindrome(s string) string {
    res := ""
    for i := 0; i < len(s); i++ {
        left, right := i, i
        for ;left >= 0 && right < len(s); {
            if s[left] != s[right] {
                break
            }
            left--
            right++
        }
        if right - left - 1 > len(res) {
            res = s[left+1: right]
        }
        //println(i, left, right, res)
        if i + 1 < len(s) && s[i] == s[i+1] {
            left, right = i, i + 1
            for ;left >= 0 && right < len(s); {
                if s[left] != s[right] {
                    break
                }
                left--
                right++
            }
            if right - left - 1 > len(res) {
                res = s[left + 1: right]
            }
        }
    }
    return res
}


func main() {
    s := "babad"
    println(s, longestPalindrome(s))

    s = "aaa"
    println(s, longestPalindrome(s))

    s = ""
    println(s, longestPalindrome(s))

    s = "a"
    println(s, longestPalindrome(s))
}

