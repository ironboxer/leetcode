/*

https://leetcode.com/problems/palindrome-pairs/


Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i] <= 300
words[i] consists of lower-case English letters.

*/


package main


import "fmt"


/*
func check(s string) bool {
    left, right := 0, len(s) - 1
    for left < right {
        if s[left] != s[right] {
            return false
        }
        left++
        right--
    }
    return true
}


func palindromePairs(words []string) [][]int {
    res := make([][]int, 0)
    for i := 0; i < len(words); i++ {
        for j := 0; j < len(words); j++ {
            if i == j {
                continue
            }
            s := words[i] + words[j]
            if check(s) {
                res = append(res, []int{i, j})
            }
        }
    }
    return res
}
*/

import "strings"


func reverse(s string) string {
    var sb strings.Builder
    runes := []rune(s)
    for i := len(runes) - 1; i >= 0; i-- {
        sb.WriteRune(runes[i])
    }
    return sb.String()
}


func palindromePairs(words []string) [][]int {
    dict := make(map[string]int)
    for i, word := range words {
        dict[word] = i
    }
    res := make([][]int, 0)
    for i, word := range words {
        wordRe := reverse(word)
        if pos, ok := dict[wordRe]; ok && pos != i {
            res = append(res, []int{i, pos})
        }
        if pos, ok := dict[""]; ok && len(word) > 0 && wordRe == word {
            res = append(res, []int{i, pos})
            res = append(res, []int{pos, i})
        }
        for k := 1; k < len(word); k++ {
            s1, s2 := word[:k], word[k:]
            s1Re, s2Re := reverse(s1), reverse(s2)
            if pos, ok := dict[s2Re]; ok && s1Re == s1 {
                res = append(res, []int{pos, i})
            }
            if pos, ok := dict[s1Re]; ok && s2Re == s2 {
                res = append(res, []int{i, pos})
            }
        }
    }
    return res
}



func main() {
    words := []string{"abcd","dcba","lls","s","sssll"}
    fmt.Println(palindromePairs(words))

    words = []string{"bat","tab","cat"}
    fmt.Println(palindromePairs(words))

    words = []string{"a", ""}
    fmt.Println(palindromePairs(words))
}
