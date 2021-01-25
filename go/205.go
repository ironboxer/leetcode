/*

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.


*/

package main


import "fmt"


func isIsomorphic(s string, t string) bool {
    m, n := len(s), len(t)
    if m != n {
        return false
    }
    A, B, C := make(map[byte]int), make(map[byte]int), make(map[byte]byte)
    for i := 0; i < m; i++ {
        val, ok := C[s[i]]
        if ok && val != t[i] {
            return false
        }
        C[s[i]] = t[i]
    }
    for i := 0; i < m; i++ {
        c := s[i]
        v, ok := A[c]
        if !ok {
            v = 0
        }
        A[c] = v + 1
    }
    for i := 0; i < m; i++ {
        c := t[i]
        v, ok := B[c]
        if !ok {
            v = 0
        }
        B[c] = v + 1
    }
    for k, v := range A {
        vv, ok := B[C[k]]
        if !ok || vv != v {
            return false
        }
    }
    return true
}

func main() {
    s := "paper"
    t := "title"
    fmt.Println(isIsomorphic(s, t))

    s = "abba"
    t = "abab"
    fmt.Println(isIsomorphic(s, t))

}
