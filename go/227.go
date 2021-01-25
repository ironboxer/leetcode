/*

https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

*/


package main


import "fmt"


func calculate(s string) int {
    left, right := 0, len(s) - 1
    // trim left space
    for s[left] == ' ' {
        left++
    }
    // trim right space
    for s[right] == ' ' {
        right--
    }
    nums := make([]int, 0)
    ops := make([]byte, 0)
    n := 0
    for i := left; i <= right; i++ {
        c := s[i]
        if c == '+' || c == '-' || c == '*' || c == '/' {
            nums = append(nums, n)
            n = 0
            ops = append(ops, c)
        } else if c == ' ' {
            // do nothing
        } else {
            n = n * 10 + int(c - '0')
        }
    }
    nums = append(nums, n)

    for len(ops) > 0 {
        op1 := ops[0]
        ops = ops[1:]
        if (op1 == '+' || op1 == '-') && len(ops) > 0 && (ops[0] == '*' || ops[0] == '/') {
            op2 := ops[0]
            a := nums[0]
            b := nums[1]
            c := nums[2]
            d := 0
            if op2 == '*' {
                d = b * c
            } else {
                d = b / c
            }
            nums[1] = a
            nums[2] = d
            nums = nums[1:]
            ops[0] = op1 
        } else {
            a := nums[0]
            b := nums[1]
            c := 0
            if op1 == '+' {
                c = a + b
            } else if op1 == '-' {
                c = a - b
            } else if op1 == '*' {
                c = a * b
            } else {
                c = a / b
            }
            nums[1] = c
            nums = nums[1:]
        }
    }
    return nums[0]
}


func main() {
    s := "100 + 200 + 300 / 100"
    fmt.Println(calculate(s))

    s = "100 * 2 / 1 + 3 * 2"
    fmt.Println(calculate(s))

    s = " 3+5 / 2 "
    fmt.Println(calculate(s))

    s = " 3/2 "
    fmt.Println(calculate(s))

    s = "3+2*2"
    fmt.Println(calculate(s))

    s = "12-3*4"
    fmt.Println(calculate(s))

}
