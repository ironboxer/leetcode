/*

https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0


The idea is very simple:

last bit of (odd number & even number) is 0.
when m != n, There is at least an odd number and an even number, so the last bit position result is 0.
Move m and n rigth a position.
Keep doing step 1,2,3 until m equal to n, use a factor to record the iteration time.
*/


package main


import "fmt"


func rangeBitwiseAnd(m int, n int) int {
    var steps uint = 0
    for m != n {
        m = m >> 1
        n = n >> 1
        steps++
    }
    fmt.Println(m, steps)
    return int(uint(m) << steps)
}


func main() {
    m, n := 5, 7
    fmt.Println(rangeBitwiseAnd(m, n))
}
