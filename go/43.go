/*

https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

*/

package main

import "fmt"
import "strings"
import "strconv"


func multiply(num1 string, num2 string) string {
    m, n := len(num1), len(num2)
    buf := make([]int, m + n + 1)
    A, B := make([]int, m), make([]int, n)
    for i := 0; i < m; i++ {
        A[i] = int(num1[m - 1 - i] - '0')
    }
    for i := 0; i < n; i++ {
        B[i] = int(num2[n - 1 - i] - '0')
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            buf[i + j] = buf[i + j] + A[i] * B[j]
        }
    }
    t := 0
    for i := 0; i < m + n + 1; i++ {
        r := buf[i] + t
        buf[i] = r % 10
        t = r / 10
    }
    res := make([]string, m + n + 1)
    for i := 0; i < m + n + 1; i++ {
        res[i] = strconv.Itoa(buf[m + n - i])
    }
    s := strings.Join(res, "")
    for i := 0; i < len(s); i++ {
        if rune(s[i]) != '0' {
            return s[i:]
        }
    }
    return "0"
}


func main() {
    num1 := "2"
    num2 := "3"
    fmt.Println(num1, num2, multiply(num1, num2))

    num1 = "123"
    num2 = "456"
    fmt.Println(num1, num2, multiply(num1, num2))

}
