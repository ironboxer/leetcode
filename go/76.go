/*

https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

*/

package main


import "fmt"


func minWindow(s string, t string) string {
    m, n := len(s), len(t)
    dict := make(map[byte]int)
    for i := 0; i < n; i++ {
        e := t[i]
        if v, ok := dict[e]; ok {
            dict[e] = v + 1
        } else {
            dict[e] = 1
        }
    }
    res := [2]int{-1, -1}
    memo := make(map[byte]int)
    counter := 0
    last := 0
    for i := 0; i < m; i++ {
        e := s[i]
        v, ok := memo[e]
        if ok {
            memo[e] = v + 1
        } else {
            memo[e] = 1
        }
        if cnt, ext := dict[e]; ext {
            if memo[e] == cnt {
                counter++
                for counter == len(dict) && last <= i {
                    if res[0] == -1 || i - last < res[1] - res[0] {
                        res[0] = last
                        res[1] = i
                    }
                    ee := s[last]
                    memo[ee]--
                    if vv, es := dict[ee]; es && memo[ee] < vv {
                        counter--
                    }
                    last++
                }
            }
        }
    }
    if res[0] != -1 {
        return s[res[0]: res[1] + 1]
    }
    return ""
}


func main() {
    S := "ADOBECODEBANC"
    T := "ABC"
    fmt.Println(minWindow(S, T))

    S = "bba"
    T = "ab"
    fmt.Println(minWindow(S, T))

}
