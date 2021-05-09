/*

https://leetcode.com/problems/generate-parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

*/

package main


import "fmt"


func generateParenthesis(n int) []string {
    res := make([]string, 0)
    var f func (s string, left int, right int)
    f = func(s string, left int, right int) {
        if n * 2 == len(s) {
            res = append(res, s)
            return
        }
        // 根据最基本的规则推出
        // 这是最简单的版本 其他的版本总是比这个版本要复杂
        if left < n {
            f(s + "(", left + 1, right)
        }
        if right < left {
            f(s + ")", left, right + 1)
        }
    }
    f("", 0, 0)
    return res
}


func main() {
    for i := 1; i < 5; i++ {
        fmt.Println(i, generateParenthesis(i))
    }
}
