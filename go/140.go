/*

https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

*/

package main


import "fmt"
import "strings"


func wordBreak(s string, wordDict []string) []string{
    memo := make(map[string][]string)
    var f func(str string) []string
    f = func(str string) []string {
        val, ok := memo[str]
        if ok {
            return val
        }
        buf := make([]string, 0)
        for _, w := range wordDict {
            if strings.HasPrefix(str, w) {
                if len(str) == len(w) {
                    buf = append(buf, w)
                } else {
                    items := f(str[len(w):])
                    // go 的这个地方太trick了
                    for _, item := range items {
                        tmp := w + " " + item
                        //items[i] = w + " " + item
                        //fmt.Println(tmp == items[i])
                        buf = append(buf, tmp)
                    }
                }
            }
        }
        memo[str] = buf
        return buf
    }
    return f(s)
}


// 写对这个代码太麻烦了

func main() {
    s := "catsanddog"
    wordDict := []string{"cat", "cats", "and", "sand", "dog"}
    fmt.Println(wordBreak(s, wordDict))

    s = "pineapplepenapple"
    wordDict = []string{"apple", "pen", "applepen", "pine", "pineapple"}
    fmt.Println(wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = []string{"cats", "dog", "sand", "and", "cat"}
    fmt.Println(wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = []string{"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}
    fmt.Println(wordBreak(s, wordDict))

}
