/*

https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

*/


package main


import "fmt"


func parse(s string) []string {
    tokens := make([]string, 0)
    n := ""
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c == ' ' {
            // pass
        } else if c == '+' || c == '-' || c == '*' {
            if len(n) > 0 {
                tokens = append(tokens, n)
                n = ""
            }
            tokens = append(tokens, string([]byte{c}))
        } else {
            n = n + string([]byte{c})
        }
    }
    if len(n) > 0 {
        tokens = append(tokens, n)
    }
    return tokens
}



func calculate(op string, a, b int) int {
    if op == "+"  {
        return a + b
    }
    if op == "-" {
        return a - b
    }
    return a * b
}


func diffWaysToCompute(input string) []int {
    vals := make([]int, 0)
    ops := make([]string, 0)
    tokens := parse(input)
    fmt.Println(tokens)
    for _, token := range tokens {
        if token == "+" || token == "-" ||  token == "*" {
            ops = append(ops, token)
        } else {
            t := 0
            for i := 0; i < len(token); i++ {
                t = t * 10 + int(token[i] - '0')
            }
            vals = append(vals, t)
        }
    }
    fmt.Println(ops, vals)

    // 本质上是构建一棵二叉排序树?
    // 为什么你想不到这个算法呢?
    // 或者是说你为什么建立不起来这个联系呢?
    var f func(left, right int) []int
    f = func(left, right int) []int {
        if left == right {
            return []int{vals[left]}
        } 
        res := make([]int, 0)
        for i := left; i < right; i++ {
            a := f(left, i)
            b := f(i+1, right)
            for _, p := range a {
                for _, q := range b {
                    c := calculate(ops[i], p, q)
                    res = append(res, c)
                }
            } 
        }
        return res
    }
    return f(0, len(vals) - 1) 
}


func main() {
    s := "2*3-4*5"
    fmt.Println(diffWaysToCompute(s))
}
