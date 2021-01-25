/*

https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

*/


package main


import "fmt"


func max(a, b int) int {
    if a >= b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a <= b {
        return a
    }
    return b
}


func addBinary(a string, b string) string {
    m, n := len(a), len(b)
    A, B := make([]byte, m), make([]byte, n)
    for i := 0; i < m; i++ {
        A[m - 1 - i] = a[i] - 48
    }
    for i := 0; i < n; i++ {
        B[n - 1 - i] = b[i] - 48
    }
    buf := make([]byte, max(m, n) + 1)
    var t byte = 0
    j := 0
    for ;j < min(m, n); j++ {
        r := A[j] + B[j] + t
        buf[j] = r % 2
        t = r / 2
    }
    for ;j < m; j++ {
        r := A[j] + t
        buf[j] = r % 2
        t = r / 2
    }
    for ;j < n; j++ {
        r := B[j] + t
        buf[j] = r % 2
        t = r / 2
    }
    if t > 0 {
        buf[len(buf) - 1] = t
    } else {
        buf = buf[:len(buf) - 1]
    }
    for i := 0; i < len(buf); i++ {
        buf[i] = buf[i] + 48
    }
    left, right := 0, len(buf) - 1
    for left < right {
        buf[left], buf[right] = buf[right], buf[left]
        left++
        right--
    }
    s := string(buf)
    //fmt.Println(buf, s)
    return s
}


func main() {
    a := "11"
    b := "1"
    fmt.Println(addBinary(a, b))

    a = "1010"
    b = "1011"
    fmt.Println(addBinary(a, b))
}
