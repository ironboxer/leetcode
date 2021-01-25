/*

https://leetcode.com/problems/maximum-product-of-word-lengths/


Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

*/


package main


import "fmt"


func isJoin(A, B map[byte]bool) bool {
    for k, _ := range A {
        _, ok := B[k] 
        if ok {
            return true
        }
    }
    for k, _ := range B {
        _, ok := A[k]
        if ok {
            return true
        }
    }
    return false
}


func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}


func maxProduct(words []string) int {
    buf := make([]map[byte]bool, 0)
    for _, word := range words {
        dict := make(map[byte]bool)
        for j := 0; j < len(word); j++ {
            c := word[j]
            dict[c - 'a'] = true
        }
        buf = append(buf, dict)
    }

    maxVal := 0
    for i := 0; i < len(buf); i++ {
        for j := i + 1; j < len(buf); j++ {
            A, B := buf[i], buf[j]
            if isJoin(A, B) {
                continue
            }
            maxVal = max(maxVal, len(words[i]) * len(words[j]))
        }
    }
    return maxVal
}

func main() {
    words := []string{"abcw","baz","foo","bar","xtfn","abcdef"}
    fmt.Println(maxProduct(words))

    words = []string{"a","ab","abc","d","cd","bcd","abcd"}
    fmt.Println(maxProduct(words))

    words = []string{"a","aa","aaa","aaaa"}
    fmt.Println(maxProduct(words))

    words = []string{"eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"}
    fmt.Println(maxProduct(words))

}
