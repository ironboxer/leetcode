/*

https://leetcode.com/problems/shortest-palindrome/

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"

*/


package main


import "fmt"

import "strings"


func reverse(s string) string {
    r := []rune(s)   
    for i, j := 0, len(r) - 1; i < j; i, j = i + 1, j - 1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}



//  非常巧妙的做法
func shortestPalindrome(s string) string {
    r := reverse(s)
    for i := 0; i < len(s) + 1; i++ {
        if strings.HasPrefix(s, r[i:]) {
            return r[:i] + s 
        }
    }
    return ""
}


func main() {
    s := "aacecaaa"
    fmt.Println(shortestPalindrome(s))

}

