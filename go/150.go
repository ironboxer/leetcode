/*

https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

*/

package main



import "fmt"
import "strconv"


func evalRPN(tokens []string) int {
    stack := make([]int, 0)
    for _, t := range tokens {
        if t == "+" || t == "-" || t == "*" || t == "/" {
            b := stack[len(stack) - 1]
            a := stack[len(stack) - 2]
            stack = stack[:len(stack) - 2]
            c := 0
            if t == "+" {
                c = a + b
            } else if t == "-" {
                c = a - b
            } else if t == "*" {
                c = a * b
            } else if t == "/" {
                c = a / b
            }
            stack = append(stack, c)
        } else {
            c, _ := strconv.Atoi(t)
            stack = append(stack, c)
        }
    }
    return stack[0]
}


func main() {
    tokens := []string{"2", "1", "+", "3", "*"}
    fmt.Println(evalRPN(tokens))
    
    tokens = []string{"4", "13", "5", "/", "+"}
    fmt.Println(evalRPN(tokens))

    tokens = []string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}
    fmt.Println(evalRPN(tokens))

}
