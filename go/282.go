/*

https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

*/

package main


import "fmt"
import "strconv"


func str2int(s string) int {
    v, err := strconv.Atoi(s)
    if err != nil {
        return -1
    }
    return v
}


func int2str(n int) string {
    return strconv.Itoa(n)
}


func addOperators(num string, target int) []string {
    res := make([]string, 0)
    var f func(path string, pos int, eval int, multed int)
    f = func(path string, pos int, eval int, multed int) {
        if pos == len(num) {
            if target == eval {
                res = append(res, path)
            }
            return
        }
        for i := pos; i < len(num); i++ {
            if i != pos && num[pos] == '0' {
                break
            }
            cur := num[pos: i+1]
            curVal := str2int(cur)
            if pos == 0 {
                f(path + cur, i + 1, curVal, curVal)
            } else {
                f(path + "+" + cur, i + 1, eval + curVal, curVal)
                f(path + "-" + cur, i + 1, eval - curVal, -curVal)
                f(path + "*" + cur, i + 1, eval - multed + multed * curVal, multed * curVal)
            }
        }
    }
    if len(num) > 0 {
        f("", 0, 0, 0)
    }
    return res
}


func main() {
    num := "123"
    target := 6
    fmt.Println(addOperators(num, target))
}
