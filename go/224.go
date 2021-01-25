/*

https://leetcode.com/problems/basic-calculator/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

*/

package main


import "fmt"
import "strconv"


func isNumber(s string) bool {
    if _, err := strconv.Atoi(s); err == nil {
        return true
    }
    return false
}


func str2Int(s string) int {
    val, _ := strconv.Atoi(s)
    return val
}


func opBy(op string, a, b int) int {
    if op == "+" {
        return a + b
    }
    if op == "-" {
        return a - b
    }
    if op == "*" {
        return a * b
    }
    return a / b
}


func peek(stack []string) string {
    length := len(stack)
    if length > 0 {
        return stack[length - 1]
    }
    return ""
}


func applyOperator(operators *[]string, values *[]int) {
    opLen, vaLen := len(*operators), len(*values)
    op := (*operators)[opLen - 1]
    *operators = (*operators)[:opLen - 1]
    b := (*values)[vaLen - 1]
    a := (*values)[vaLen - 2]
    c := opBy(op, a, b)
    (*values)[vaLen - 2] = c
    *values = (*values)[:vaLen - 1]
}


func greaterPrecedence(op1, op2 string) bool {
    if op2 == "+" || op2 == "-" {
        return true
    }
    if op1 == "+" || op1 == "-" {
        return false
    }
    return true
}


func parse(s string) []string {
    tokens := make([]string, 0)
    n := ""
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c == ' ' {
            // nothing
        } else if c == '+' || c == '-' || c == '*' || c == '/' {
            if len(n) > 0 {
                tokens = append(tokens, n)
                n = ""
            }
            tokens = append(tokens, string([]byte{c}))
        } else if c == '(' {
            if len(n) > 0 {
                tokens = append(tokens, n)
                n = ""
            }
            tokens = append(tokens, string([]byte{c})) 
        } else if c == ')' {
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
        n = ""
    }
    return tokens
}


func calculate2(s string) int {
    tokens := parse(s)
    values := make([]int, 0)
    operators := make([]string, 0)
    for _, token := range tokens {
        if isNumber(token) {
            values = append(values, str2Int(token))
        } else if token == "(" {
            operators = append(operators, token)
        } else if token == ")" {
            for top := peek(operators); top != "" && top != "("; top = peek(operators) {
                applyOperator(&operators, &values)
            }
            operators = operators[:len(operators) - 1]
        } else {
            //fmt.Println(operators, values)
            for top := peek(operators); top != "" && top != "(" && top != ")" && greaterPrecedence(top, token); top = peek(operators) {
                applyOperator(&operators, &values)
            }
            operators = append(operators, token)
        }
    }
    for top := peek(operators); top != ""; top = peek(operators) {
        applyOperator(&operators, &values)
    }
    return values[0]
}


// 想要完全做对也是不太容易啊


func calculate(s string) int {
    var r = 0
    var sign = 1
    var n = ""
    var i = 0
    var total = len(s)
    
    for i < total {
        var c = rune(s[i])
        if c == '(' {
            if len(n) > 0 {
                r = r + sign * str2Int(n)
                n = ""
            }
            var j = i + 1
            var cnt = 1
            for cnt > 0 && j < total {
                if rune(s[j]) == ')' {
                    cnt--
                } else if rune(s[j]) == '(' {
                    cnt++
                }
                j++
            }
            var t = calculate(s[i+1:j-1])
            r = r + sign * t
            i = j - 1
        } else if c == ' ' {

        } else if c == '+' {
            if len(n) > 0 {
                r = r + sign * str2Int(n)
                n = ""
            }
            sign = 1
        } else if c == '-' {
            if len(n) > 0 {
                r = r + sign * str2Int(n)
                n = ""
            }
            sign = -1
        } else {
            n = n + string(c)
        }
        i++
    }
    if len(n) > 0 {
        r = r + sign * str2Int(n)
        n = ""
    }
    return r
}

func main() {
    s := calculate("1+2-3+4")
    fmt.Println(s)

    s = calculate("(1+(4+5+2)-3)+(6+8)")
    fmt.Println(s)

    s = calculate("1 + 1")
    fmt.Println(s)

    s = calculate("(6)-(8)-(7)+(1+(6))")
    fmt.Println(s)

    s = calculate("(6)-(8)-(7)")
    fmt.Println(s)

    s = calculate("6-7-8")
    fmt.Println(s)

}

