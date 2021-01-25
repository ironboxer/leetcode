/*

https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false

*/


package main


import "fmt"


func isPowerOfTwo(n int) bool {
    m := uint(n)
    var v uint = 0
    var i uint = 0
    for i < 31 {
        v = 1 << i
        if v == m {
            return true
        }
        if v > m {
            return false
        }
        i++
    } 

    return false
}


func main() {
    for i := 0; i < 10000; i++ {
        if isPowerOfTwo(i) {
            fmt.Println(i)
        }
    }
}
