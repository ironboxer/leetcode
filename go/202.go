/*

https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

*/


package main

import "fmt"

func isHappy(n int) bool {
    for i := 0; i < 100; i++ {
        r := 0
        for n != 0 {
            t := n % 10
            r = r + t * t
            n = n / 10
        }
        if r == 1 {
            return true
        }
        n = r
    }
    return false
}


func main() {
    for i := 1; i < 20; i++ {
        fmt.Println(i, isHappy(i))
    }
}
