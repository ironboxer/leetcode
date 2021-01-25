/*

https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]


https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution

*/


package main


import "fmt"


// 这道题确实有点难 它在技术上并没有什么特别的突破 但是实现细节上更加复杂

// pending
// 稍微有点复杂
func removeInvalidParentheses(s string) []string {

}


func main() {
    s := "(a)())()"
    fmt.Println(removeInvalidParentheses(s))
}

