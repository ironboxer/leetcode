/*

https://leetcode.com/problems/find-the-difference/


Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

*/

package main


import "fmt"



func findTheDifference(s string, t string) byte {
    A, B := make(map[byte]int), make(map[byte]int)
    for i := 0; i < len(s); i++ {
        c := s[i]
        v, ok := A[c]
        if !ok {
            v = 0
        }
        A[c] = v + 1
    }
    for i := 0; i < len(t); i++ {
        c := t[i]
        v, ok := B[c]
        if !ok {
            v = 0
        }
        B[c] = v + 1
    }
    for key, val := range B {
        val2, ok := A[key]
        if !ok || val != val2 {
            return key
        }
    }
    return byte(0)
}


func main() {
    s := "abcd"
    t := "abcde"    
    fmt.Println(findTheDifference(s, t))

    s = "a"
    t = "aa"
    fmt.Println(findTheDifference(s, t))

}
