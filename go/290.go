/*

https://leetcode.com/problems/word-pattern/


Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

bijection: 双射

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

*/


package main


import "fmt"
import "strings"


func wordPattern(pattern string, s string) bool {
    list := strings.Split(s, " ")
    if len(pattern) != len(list) {
        return false
    }
    A, B := make(map[byte]string), make(map[string]byte)
    for i := 0; i < len(list); i++ {
        e := pattern[i]
        p := list[i]
        v1, ok1 := A[e]
        if ok1 {
            if v1 != p {
                return false
            }
        } else {
            A[e] = p
        }
        v2, ok2 := B[p]
        if ok2 {
            if v2 != e {
                return false
            }
        } else {
            B[p] = e
        }
    }
    return true
}


func main() {
    pattern := "abba"
    str := "dog cat cat dog"
    //str := "dog dog dog dog"
    fmt.Println(wordPattern(pattern, str))
}
