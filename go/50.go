/*

https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

*/

package main


import "fmt"


func myPow(x float64, n int) float64 {
    if n == 0 {
        return float64(1)
    }
    if n == 1 {
        return x
    }
    if n < 0 {
        return 1 / myPow(x, -n)
    }
    r := 1.0
    // 最多循环32次
    // 所以时间复杂度为O(1) O(1)是常数的意思
    for n != 0 {
        // n一定会经历变成1, res 也会被赋值
        if n & 1 == 1 {
            r = r *  x
        }
        x = x * x
        n = n >> 1
    }
    return r
}


func main() {
    x := 2.00000
    n := -2
    fmt.Println(myPow(x, n))

    x = 1.00000
    n = -2147483648
    fmt.Println(myPow(x, n))
}

