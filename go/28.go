/*


https://leetcode.com/problems/implement-strstr

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

*/


package main

import "fmt"


func strStr(haystack string, needle string) int {
    m, n := len(haystack), len(needle)
    if m < n {
        return -1
    }
    for i := 0; i < m - n + 1; i++ {
        flag := true
        for j := 0; j < n; j++ {
            if haystack[i + j] != needle[j] {
                flag = false
                break
            }
        }
        if flag {
            return i
        } 
    }
    return -1
}



func main() {
    haystack := "hello world"
    needle := "hello"
    fmt.Println(haystack, needle, strStr(haystack, needle))

    haystack = "abcdefg"
    needle = "de"
    fmt.Println(haystack, needle, strStr(haystack, needle))

    haystack = "a"
    needle = "a"
    fmt.Println(haystack, needle, strStr(haystack, needle))


}
