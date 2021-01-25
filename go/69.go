/*

https://leetcode.com/problems/sqrtx/

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

*/

package main


import "fmt"


/*
func mySqrt(x int) int {
    for i := 1;i <= x;i++{
        v := i * i
        if v ==  x {
            return i
        }
        if v > x {
            return i - 1
        }
    }
    return 0
}
*/


func mySqrt(x int) int {
    left, right := 1, (x + 1) / 2
    for left <= right {
        mid := left + (right - left) / 2
        val := mid * mid
        if val < x {
            left = mid + 1
        } else if val > x {
            right = mid - 1
        } else {
            return mid
        }
    } 
    return right
}


func main() {
    for i := 1; i < 100; i++ {
        fmt.Println(i, mySqrt(i))
    }
}
