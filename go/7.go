/*
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

*/

package main

/*
能把这道题做出来很不容易
*/
func reverse(x int) int {
    // 2 << 30 == 2147483648
    const MaxInt = uint(2 << 30)
    println(MaxInt)
    sign := 1
    if x < 0 {
        sign = -1
        x = -x
    }
    var r uint = 0
    for ;x != 0; {
        t := x % 10
        r = r * 10 + uint(t)
        x /= 10
    }
    if sign > 0 {
        if r <= MaxInt - 1 {
            return int(r) 
        } else {
            return 0
        }
    } else {
        if r <= MaxInt {
            return sign * int(r)
        } else {
            return 0
        }
    }
}


func main() {
    x := -123
    println(x, reverse(x))
    x = 1534236469
    println(x, reverse(x))
    x = 2147483647
    println(x, reverse(x))
}
