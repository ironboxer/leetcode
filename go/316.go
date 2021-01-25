/*

https://leetcode.com/problems/remove-duplicate-letters/


Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

*/


package main


import "fmt"


// 这道题没有看明白什么意思
// 如果完全没有看懂 抄一遍有什么意义?
func removeDuplicateLetters(s string) string {
    index := make(map[byte]int)
    for i, e := range s {
        index[e] = i
    }
    res := ""
    for i, e := range s {
        v, ok := index[e]
        if ok {
            continue
        }

    }
}


func main() {

}

